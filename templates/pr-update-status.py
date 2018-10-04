# -*- coding: utf-8 -*-
# (gforcada) This file is here as running it as a separate build step on
# Jenkins does not work, see:
# https://github.com/plone/jenkins.plone.org/blob/master/scripts/pr-get-info.py
from github import Github
from github.GithubException import BadCredentialsException
from github.GithubException import UnknownObjectException

import os
import re
import sys


def error(message):
    print(
        '\n\n\n'
        f'{message}'
        '\n'
        'Please contact the testing team: '
        'https://github.com/orgs/plone/teams/testing-team'
        '\n'
        'Fill an issue as well: '
        'https://github.com/plone/jenkins.plone.org/issues/new'
        '\n\n\n'
    )
    sys.exit(1)


job_name = os.environ['JOB_NAME']
tests_folder = 'parts/test/testreports'
if '4.3' in job_name:
    tests_folder = 'parts/jenkins-test/testreports'

PR_RE = r'https://github.com/(.*)/(.*)/pull/(.*)'
job_run_successfully = True

# bare basic way to know if there was any test failure
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
    error('GITHUB_API_KEY does not exist, pull requests can not be updated.')

pull_request_urls = os.environ['PULL_REQUEST_URL']
build_url = os.environ['BUILD_URL']
g = Github(github_api_key)

for pr in pull_request_urls.split():
    org, repo, pr_number = re.search(PR_RE, pr).groups()

    pr_number = int(pr_number)

    # get the pull request organization it belongs to
    try:
        g_org = g.get_organization(org)
    except BadCredentialsException:
        error('The API key used seems to not be valid any longer.')
    except UnknownObjectException:
        error(
            f'Error on trying to get info from Pull Request {pr}'
            '\n'
            f'The organization "{org}" does not seem to exist.'
        )

    # the repo where the pull request is from
    try:
        g_repo = g_org.get_repo(repo)
    except UnknownObjectException:
        error(
            f'Error on trying to get info from Pull Request {pr}'
            '\n'
            f'The repository "{repo}" does not seem to exist.'
        )

    # the pull request itself
    try:
        g_pr = g_repo.get_pull(pr_number)
    except UnknownObjectException:
        error(
            f'Error on trying to get info from Pull Request {pr}'
            '\n'
            f'The pull request num "{pr_number}" does not seem to exist.'
        )

    # get the branch
    branch = g_pr.head.ref

    # report back to github about how the job finished
    last_commit = g_pr.get_commits().reversed[0]
    status = u'success'
    if not job_run_successfully:
        status = u'error'

    last_commit.create_status(
        status,
        target_url=build_url,
        description=f'Job finished with {status} status',
        context=f'Plone Jenkins CI - {job_name}',
    )
