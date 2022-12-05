# Release notes for Plone 6.0.0rc2

Release date: Monday December 5, 2022.

Release schedule: https://plone.org/download/release-schedule

For technical wizards who want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0.0rc2/constraints.txt](https://dist.plone.org/release/6.0.0rc1/constraints.txt)
* With Buildout you can use the versions file at https://dist.plone.org/release/6.0.0rc2/versions.cfg plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0.0rc2/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0.0rc2/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.0rc1:

* None really.  Lots of packages have gotten a final release, losing their alpha, beta or release candidate markers.

We are in a bugfix-only mode.  An upgrade from rc1 to rc2 should be painless and is recommended for everyone.


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


## Final release date: December 12, 2022

Unless blocking issues are found that require more work, we expect to release Plone 6.0.0 final one week from now:
December 12, 2022.

If you find any issues, blocking or not, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
