# -*- coding: utf-8 -*-
# (gforcada) This file is here as running it as a separate build step on
# Jenkins does not work, see:
# https://github.com/plone/jenkins.plone.org/blob/master/scripts/addon-get-info.py
from github import Github
from github.GithubException import BadCredentialsException
from github.GithubException import UnknownObjectException

import os
import sys


job_name = os.environ['JOB_NAME']
build_url = os.environ['BUILD_URL']
github_org = os.environ['ADDON_GITHUB_ORG']
addon_name = os.environ['ADDON_NAME']
latest_commit = os.environ['GITHUB_LATEST_COMMIT']

tests_folder = 'parts/test/testreports'


# bare basic way to know if there was any test failure
job_run_successfully = True
try:
    files = [f for f in os.listdir(tests_folder)]
except OSError:
    files = []
    job_run_successfully = False

for f in files:
    with open('{0}/{1}'.format(tests_folder, f)) as xml_file:
        first_line = xml_file.read().split('\n')[0]
        failures = True
        if first_line.find('failures="0"') != -1:
            failures = False
        errors = True
        if first_line.find('errors="0"') != -1:
            errors = False

        if failures or errors:
            job_run_successfully = False
            break

try:
    github_api_key = os.environ['GITHUB_API_KEY']
except KeyError:
    print(
        '\n\n\n'
        'GITHUB_API_KEY does not exist, add-ons can not be notified. '
        '\n'
        'Please contact the testing team: '
        'https://github.com/orgs/plone/teams/testing-team'
        '\n'
        'Fill an issue as well: '
        'https://github.com/plone/jenkins.plone.org/issues/new'
        '\n\n\n'
    )
    sys.exit(0)

g = Github(github_api_key)

# get the pull request organization it belongs to
try:
    g_org = g.get_organization(github_org)
except BadCredentialsException:
    print(
        '\n\n\n'
        'The API key used seems to not be valid any longer.'
        '\n'
        'Please contact the testing team: '
        'https://github.com/orgs/plone/teams/testing-team'
        '\n'
        'Fill an issue as well: '
        'https://github.com/plone/jenkins.plone.org/issues/new'
        '\n\n\n'
    )
    sys.exit(0)
except UnknownObjectException:
    msg = (
        '\n\n\n'
        'Error on trying to get github organization %s '
        'it does not seem to exist.'
        '\n\n\n'
    )
    print(msg % github_org)
    sys.exit(0)

# the repo where the pull request is from
try:
    g_repo = g_org.get_repo(addon_name)
except UnknownObjectException:
    msg = (
        '\n\n\n'
        'Error on trying to get info from repository %s '
        'it does not seem to exist.'
        '\n\n\n'
    )
    print(msg % addon_name)
    sys.exit(0)

# the pull request itself
try:
    g_commit = g_repo.get_commit(latest_commit)
except UnknownObjectException:
    msg = (
        '\n\n\n'
        'Error on trying to get commit %s on repository %s '
        'it does not seem to exist.'
        '\n\n\n'
    )
    print(msg % (latest_commit, addon_name))
    sys.exit(0)

status = u'Your add-on is compatible!'
if not job_run_successfully:
    status = u'Unfortunately there seems to be some tests failing.'

header = 'Jenkins CI reporting about add-on compatibility.'
footer = 'See the full report here: %s' % build_url
comment = '%s - %s\n**%s**\n%s' % (
    header,
    job_name,
    status,
    footer,
)
g_commit.create_comment(
    body=comment
)
