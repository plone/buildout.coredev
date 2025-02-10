# Release notes for Plone 6.2.0a1 (unreleased)

* Last updated: February, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2.0a1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2.0a1/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2.0a1/constraints.txt](https://dist.plone.org/release/6.2.0a1/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2.0a1/versions.cfg](https://dist.plone.org/release/6.2.0a1/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2.0a1/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2.0a1/versions-ecosystem.cfg).
* Use Docker image `plone-backend` 6.2.0a1.


## Highlights

These are the main changes since 6.1.0:

* nothing yet


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.2 is meant to be used with Volto 18.
Latest release is [18.8.1](https://www.npmjs.com/package/@plone/volto/v/18.8.1).  See the [changelog](https://github.com/plone/volto/blob/18.8.1/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
packaging==24.2
pip==24.3.1
setuptools==75.6.0
wheel==0.45.1
zc.buildout==4.0
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that `zc.buildout` 4 has `packaging` as a dependency, so we added a pin for it in the requirements.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
