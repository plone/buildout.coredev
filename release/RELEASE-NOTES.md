# Release notes for Plone 6.0.16 (unreleased)

* Last updated: April 4, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Last maintenance release

Plone 6.0.15 was the last regularly scheduled maintenance release of Plone 6.0. We might do another release a few months from now if it makes sense, but we don't guarantee this. Plone 6.0 has had two years of maintenance support, and meanwhile Plone 6.1 is out. You are encouraged to upgrade.

Plone 6.0 (and any Plone 6 minor release) still gets security support until the end of 2027.


## Highlights

Major changes since 6.0.15:

* `twine`: Add compatibility with setuptools 77+.
  This fixes errors when making releases to PyPI: "twine.exceptions.InvalidDistribution: Metadata is missing required fields: Name, Version." .
* `plone.recipe.zope2instance`: Check for presence of Products.CMFPlone with multiple keys.  This is needed, depending on the used `zc.buildout` and `setuptools` versions.
* `plone.scale`: Add method to 'scale' SVGs by modifying display size and viewbox.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.33.0](https://www.npmjs.com/package/@plone/volto/v/16.33.0).  See the [changelog](https://github.com/plone/volto/blob/16.33.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

Note that Volto 17 and 18 are also available, and you can use them on Plone 6.0, but we will keep recommending Volto 16 by default.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.9, 3.10, 3.11, 3.12, and 3.13.

Using Python 3.8 will fail.


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
