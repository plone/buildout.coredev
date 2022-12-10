# Release notes for Plone 6.0.0 final (unreleased)

Last updated: Saturday December 10, 2022.

Release schedule: https://plone.org/download/release-schedule

Upgrade guide: https://6.docs.plone.org/upgrade/index.html

For technical wizards who want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at https://dist.plone.org/release/6.0-dev/versions.cfg plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.0rc2:

* Several bug fixes.  See details in the changelog.


## Volto frontend

The default frontend for Plone 6 is Volto. Latest release is [16.3.0](https://www.npmjs.com/package/@plone/volto/v/16.3.0).  See the [changelog](https://github.com/plone/volto/blob/16.3.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.
The ClassicUI is still available when you only run the Python process.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.


## Installation

For installation instructions, see the [documentation](https://6.dev-docs.plone.org/install/index.html).
This documentation is under development, but this should get you up and running.  No worries.
We expect to switch https://docs.plone.org to show the Plone 6 documentation sometime this week.


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
