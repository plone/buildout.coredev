# Release notes for Plone 6.2.0a1 (unreleased)

* Last updated: September 10th, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* TODO Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.1.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2-dev/constraints.txt](https://dist.plone.org/release/6.2-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2-dev/versions.cfg](https://dist.plone.org/release/6.2-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes compared to 6.1:

* Move to src-layout for a lot of packages.  This is ongoing.  An internal thing.
* Some templates are being moved to `plone.app.layout`, this is ongoing.  Progress so far:
  * Moved lock info viewlet from `plone.locking`.
  * Modify `plone.protect.confirm` to use a simpler template that does not assume Classic UI is installed.
    The previous template was moved to `plone.app.layout`.
* The plan is also to switch to native namespaces for `plone.*` and `Products.*`.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.2 is meant to be used with Volto 18.
Latest release is [18.25.0](https://www.npmjs.com/package/@plone/volto/v/18.25.0).  See the [changelog](https://github.com/plone/volto/blob/18.25.0/packages/volto/CHANGELOG.md).
You can already test with the [latest Volto 19 alpha version](https://github.com/plone/volto/blob/main/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
packaging==25.0
pip==25.1.1
setuptools==80.9.0
wheel==0.45.1
zc.buildout==4.1.12
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
