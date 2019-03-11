# -*- coding: utf-8 -*-
# (gforcada) This file is here for Jenkins jobs purposes
from github import Github
from github.GithubException import BadCredentialsException
from github.GithubException import UnknownObjectException

import os
import sys


def is_report_fine():
    if not os.path.exists('deps.txt'):
        print(
            '\n\n\n'
            'There is no deps.txt file, something went wrong'
        )
        sys.exit(0)

    is_fine = False
    with open('deps.txt') as deps_file:
        for line in deps_file.read():
            if '======' in line:
                is_fine = True

    return is_fine


def package_github_organization(package):
    org = 'plone'
    with open('sources.cfg') as sources:
        for line in sources.readlines():
            if package in line:
                if 'remotes:collective' in line:
                    org = 'collective'
                break
    return org


def _get_github_api():
    try:
        github_api_key = os.environ['GITHUB_API_KEY']
    except KeyError:
        print(
            '\n\n\n'
            'GITHUB_API_KEY does not exist, pull requests can not be updated. '
            '\n'
            'Please contact the testing team: '
            'https://github.com/orgs/plone/teams/testing-team'
            '\n'
            'Fill an issue as well: '
            'https://github.com/plone/jenkins.plone.org/issues/new'
            '\n\n\n'
        )
        sys.exit(0)
    return github_api_key


def _get_github_organization(github, organization):
    try:
        g_org = github.get_organization(organization)
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
            'Error on trying to get info from organization %s'
            '\n'
            'The organization "%s" does not seem to exist.'
            '\n\n\n'
        )
        print(msg % (organization, organization))
        sys.exit(0)
    return g_org


def _get_github_repository(g_org, package):
    try:
        g_repo = g_org.get_repo(package)
    except UnknownObjectException:
        msg = (
            '\n\n\n'
            'Error on trying to get info from repository %s'
            '\n'
            'The repository "%s" does not seem to exist.'
            '\n\n\n'
        )
        print(msg % (package, package))
        sys.exit(0)

    return g_repo


def _get_github_branch(g_repo, branch):
    try:
        g_branch = g_repo.get_branch(branch)
    except UnknownObjectException:
        msg = (
            '\n\n\n'
            'Error on trying to get info from branch %s'
            '\n'
            'The branch "%s" does not seem to exist.'
            '\n\n\n'
        )
        print(msg % (branch, branch))
        sys.exit(0)

    return g_branch


def _update_branch(g_branch, report_is_fine):
    build_url = os.environ['BUILD_URL']
    last_commit = g_branch.commit
    status = u'error'
    description = u'There are dependencies not declared'
    if report_is_fine:
        status = u'success'
        description = u'Dependencies are fine'

    last_commit.create_status(
        status,
        target_url=build_url,
        description=description,
        context='Plone Jenkins CI - dependencies tracker',
    )


def ping_github():
    report_is_fine = is_report_fine()
    package = os.environ['PACKAGE_NAME']
    branch = os.environ['BRANCH']
    organization = package_github_organization(package)
    github_api_key = _get_github_api()

    g = Github(github_api_key)
    g_org = _get_github_organization(g, organization)
    g_repo = _get_github_repository(g_org, package)
    g_branch = _get_github_branch(g_repo, branch)
    _update_branch(g_branch, report_is_fine)


ping_github()


