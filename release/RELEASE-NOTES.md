# Release notes for Plone 6.0.0.1

* Released: Monday December 19, 2022
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0.0.1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0.0.1/changelog.txt).

For technical wizards who want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0.0.1/constraints.txt](https://dist.plone.org/release/6.0.0.1/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0.0.1/versions.cfg](https://dist.plone.org/release/6.0.0.1/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0.0.1/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0.0.1/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.0:

* Zope: Security fix for a Cross Site Scripting vulnerability. See [announcement](https://community.plone.org/t/zope-4-8-4-and-5-7-1-released/15992).  The security fix is in Zope 5.7.1, but there were a few regressions, so we use 5.7.3.
* plone.protect: fix test that failed after the security fix.
* plone.volto: A few textual improvements in the default created pages and the migration wizard.


## Volto frontend

The default frontend for Plone 6 is Volto. Latest release is [16.4.0](https://www.npmjs.com/package/@plone/volto/v/16.4.0).  See the [changelog](https://github.com/plone/volto/blob/16.4.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.
The Classic UI is still available when you only run the Python process.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
