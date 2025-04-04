# Release notes for Plone 6.2.0a1 (unreleased)

* Last updated: April 4, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* TODO Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.1.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2-dev/constraints.txt](https://dist.plone.org/release/6.2-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2-dev/versions.cfg](https://dist.plone.org/release/6.2-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes compared to 6.1:

* `five.intid`, `five.customerize`, `five.localsitemanager`: Drop support for `pkg_resources` namespace and replace it with PEP 420 native namespace.
* `twine`: Add compatibility with setuptools 77+.
  This fixes errors when making releases to PyPI: "twine.exceptions.InvalidDistribution: Metadata is missing required fields: Name, Version." .
* `plone.recipe.zope2instance`: Check for presence of Products.CMFPlone with multiple keys.  This is needed, depending on the used `zc.buildout` and `setuptools` versions.
* `plone.scale`: Add method to 'scale' SVGs by modifying display size and viewbox.


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
pip==25.0.1
setuptools==75.8.2
wheel==0.45.1
zc.buildout==4.1.4
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
