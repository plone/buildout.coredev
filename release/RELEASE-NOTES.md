# Release notes for Plone 6.3.0a1 (unreleased)

TODO: not all if these links exist yet.  There is no hurry.

* Last updated: May 21st, 2026
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-63.html), explaining the biggest changes compared to 6.1.
* Canonical place for these [release notes](https://dist.plone.org/release/6.3-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.3-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.3-dev/constraints.txt](https://dist.plone.org/release/6.3-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.3-dev/versions.cfg](https://dist.plone.org/release/6.3-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.3-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.3-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes compared to 6.2:

* nothing yet


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.3 is meant to be used with Volto 19.
Latest release is [19.0.0](https://www.npmjs.com/package/@plone/volto/v/19.0.0).  See the [changelog](https://github.com/plone/volto/blob/19.0.0/packages/volto/CHANGELOG.md).

### Volto related changes in the Python backend since 6.1:

* nothing yet


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.

### Classic UI related changes since 6.1:

* nothing yet


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, 3.13, and 3.14.

TODO We probably want to drop 3.10, as it will be out of security support in October 2026.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
horse-with-no-namespace==20260202.0
pip==26.1.1
setuptools==81.0.0
wheel==0.47.0
zc.buildout==5.2.0
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
