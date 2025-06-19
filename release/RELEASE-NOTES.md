# Release notes for Plone 6.1.2 (unreleased)

* Last updated: June 20th, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1-dev/constraints.txt](https://dist.plone.org/release/6.1-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1-dev/versions.cfg](https://dist.plone.org/release/6.1-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes since 6.1.1:

* All packages in the `five` and `z3c` namespaces have dropped support for ``pkg_resources`` namespace and replaced it with PEP 420 native namespace.
  Caution: if you are using any other packages in these namespaces for which we have no versoin pin, you should switch these to versions using a PEP 420 namespace as well.
* `twine`: Add compatibility with setuptools 77+.
  This fixes errors when making releases to PyPI: "twine.exceptions.InvalidDistribution: Metadata is missing required fields: Name, Version." .
* `plone.recipe.zope2instance`: Check for presence of Products.CMFPlone with multiple keys.  This is needed, depending on the used `zc.buildout` and `setuptools` versions.
* `plone.app.dexterity`: Include `obj` in the results from the `INextPreviousProvider` adapter.
* `plone.app.discussion`:
  * Implement `auto_approve_admin_comments` based on specified roles.
  * Add Volto control panel.
* `plone.app.iterate`: Add `is_working_copy` column to catalog metadata.
* `plone.app.multilingual`: Run the SetupMultilingualSite actions with an event subscriber.
* `plone.base`:
  * Refactoring Interface ITinyMCEPluginSchema, field `menubar` is not longer a `List`, it's now a `TextLine` Field.
  * Add a "is_truthy" utility to test for true-ish and false-ish string values.
* `plone.distribution`:
  * Add attribute `package` to `plone.distribution.core.Distribution` to store which package registered a specific distribution.
  * Support specifying a base GenericSetup profile during distribution registration.
* `plone.namedfile`:
  * Add a `srcset` method to the `@@images` view.
  * "Scale" SVGs by setting the correct height and width for the given scale in its metadata.
* `plone.restapi`:
  * `@site` service: Add a way for add-ons to add additional data using an `ISiteEndpointExpander` adapter.
  * Include all summary fields when serializing `next_item` and `previous_item`.
* `plone.scale`: Add method to 'scale' SVGs by modifying display size and viewbox.
* `plone.volto`:
  * Enable automatic versioning for content types with blocks.
  * Enable preview image link behavior by default for most content types.
  * Put preview image fields in their own fieldset, and the navigation title field in the Settings fieldset.
  * Enable navigation title by default for most content types.
  * Create a separate `initial` profile which is used to set up the Volto distribution.
    The existing `default` profile defines the Volto add-on, and makes minimal changes to existing content types.
    The `initial` profile includes the `plone.app.contenttypes:default` profile and fully controls the behaviors for the included content types.
* `plonetheme.barceloneta`: Support for required and invalid styles on form tabs.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.23.0](https://www.npmjs.com/package/@plone/volto/v/18.23.0).  See the [changelog](https://github.com/plone/volto/blob/18.23.0/packages/volto/CHANGELOG.md).
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
setuptools==80.9.0
wheel==0.46.1
zc.buildout==4.1.12
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that if you use Buildout and are on `setuptools` 80+, you need the latest `zc.buildout` 4.1.12.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
