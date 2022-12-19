# Release notes for Plone 5.2.10.1

* Released: Monday December 19, 2022
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://5.docs.plone.org/manage/upgrading/version_specific_migration/upgrade_to_52.html), explaining the biggest changes compared to 5.1.
* Canonical place for these [release notes](https://dist.plone.org/release/5.2.10.1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/5.2.10.1/changelog.txt).

For technical wizards who want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/5.2.10.1/constraints.txt](https://dist.plone.org/release/5.2.10.1/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/5.2.10.1/versions.cfg](https://dist.plone.org/release/5.2.10.1/versions.cfg).


## Highlights

Major changes since 5.2.10:

* Zope: Security fix for a Cross Site Scripting vulnerability. See [announcement](https://community.plone.org/t/zope-4-8-4-and-5-7-1-released/15992).  The security fix is in Zope 4.8.4, but there were a few regressions, so we use 4.8.6.
* plone.protect: fix test that failed after the security fix.


## Python compatibility

This release supports Python 2.7, 3.7, and 3.8.

**Python 3.6 is no longer supported.**
See the [community announcement](https://community.plone.org/t/plone-5-2-drops-python-3-6-support/15706).
Note that both Python 2.7 and 3.6 have reached end of life.
This means the wider Python community no longer supports it.
For example, the default WSGI server used by Plone, which is `waitress`, has a security problem that is only solved on Python 3.7 and higher.  If you use `waitress` on earlier Python versions, you are vulnerable.

Python 3.7 will reach end of life in June 2023.
See https://devguide.python.org/versions/ for the canonical information.
It will get harder to test and support Plone on unsupported Python versions.

Especially Python 2.7 should only be used as a temporary stepping stone before you migrate your Plone site to Python 3.


## Installation

For installation instructions, see the [documentation](https://5.docs.plone.org/manage/installing/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
