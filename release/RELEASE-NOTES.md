# Release notes for Plone 5.2.10.2

* Released: Wednesday December 21, 2022
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://5.docs.plone.org/manage/upgrading/version_specific_migration/upgrade_to_52.html), explaining the biggest changes compared to 5.1.
* Canonical place for these [release notes](https://dist.plone.org/release/5.2.10.2/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/5.2.10.2/changelog.txt).

For technical wizards who want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/5.2.10.2/constraints.txt](https://dist.plone.org/release/5.2.10.2/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/5.2.10.2/versions.cfg](https://dist.plone.org/release/5.2.10.2/versions.cfg).


## Highlights

Major changes since 5.2.10.1:

* `plone.app.blocks`: Fix regression after Zope security fix. The `layout_view` was rendered as plain text instead of html.
  Note that this is not used by core Plone, but is in use by several tile-related ecosystem packages, for example Mosaic.

* Zope: revert updates to dependency package versions.

  * Plone 5.2.10 extends the versions.cfg or constraints from Zope 4.8.3.
  * Plone 5.2.10.1 extends the versions.cfg or constraints from Zope 4.8.6. This has the security fix and related regression fixes, plus lots of dependency package updates.  This includes a Datetime update which can cause problems on Python 2.  There may be other problems that we have not seen yet.
  * Plone 5.2.10.2 now extends the versions.cfg or constraints from Zope 4.8.3, and only overrides the Zope version pin to 4.8.6.  So you have the security fix and related regression fixes, but keep the dependency package versions the same as originally.


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
