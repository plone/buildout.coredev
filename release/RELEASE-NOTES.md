# Release notes for Plone 6.1.2 (unreleased)

* Last updated: June 10th, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1-dev/constraints.txt](https://dist.plone.org/release/6.1-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1-dev/versions.cfg](https://dist.plone.org/release/6.1-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes since 6.1.1:

* `twine`: Add compatibility with setuptools 77+.
  This fixes errors when making releases to PyPI: "twine.exceptions.InvalidDistribution: Metadata is missing required fields: Name, Version." .
* `plone.recipe.zope2instance`: Check for presence of Products.CMFPlone with multiple keys.  This is needed, depending on the used `zc.buildout` and `setuptools` versions.
* `plone.app.dexterity`: Include `obj` in the results from the `INextPreviousProvider` adapter.
* `plone.app.discussion`: Implement `auto_approve_admin_comments` based on specified roles.
* `plone.app.iterate`: Add `is_working_copy` column to catalog metadata.
* `plone.base`: Refactoring Interface ITinyMCEPluginSchema, field `menubar` is not longer a `List`, it's now a `TextLine` Field.
* `plone.distribution`: Add attribute `package` to `plone.distribution.core.Distribution` to store which package registered a specific distribution.
* `plone.namedfile`: Add a `srcset` method to the `@@images` view.
* `plone.restapi`: `@site` service: Add a way for add-ons to add additional data using an `ISiteEndpointExpander` adapter.
* `plone.scale`: Add method to 'scale' SVGs by modifying display size and viewbox.
* `plone.volto`:
  * Enable automatic versioning for content types with blocks.
  * Enable preview image link behavior by default for most content types.
  * Put preview image fields in their own fieldset, and the navigation title field in the Settings fieldset.
  * Enable navigation title by default for most content types.
* `plonetheme.barceloneta`: Support for required and invalid styles on form tabs.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.2 is meant to be used with Volto 18.
Latest release is [18.22.0](https://www.npmjs.com/package/@plone/volto/v/18.22.0).  See the [changelog](https://github.com/plone/volto/blob/18.22.0/packages/volto/CHANGELOG.md).
You can already test with the [latest Volto 19 alpha version](https://github.com/plone/volto/blob/main/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
packaging==25.0
pip==25.1.1
setuptools==79.0.1
wheel==0.46.1
zc.buildout==4.1.10
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that the latest Buildout release does not yet support `setuptools` 80, but that will soon change.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
