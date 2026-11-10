# Release notes for Plone 6.0.16

* Released: November 10th, 2026
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0.16/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0.16/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0.16/constraints.txt](https://dist.plone.org/release/6.0.16/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0.16/versions.cfg](https://dist.plone.org/release/6.0.16/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0.16/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0.16/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Last maintenance release

Plone 6.0.15 was the last regularly scheduled maintenance release of Plone 6.0.
The new 6.0.16 release is an exception for security reasons.

Plone 6.0 has had two years of maintenance support, and meanwhile Plone 6.1 and 6.2 are out. You are encouraged to upgrade.

Plone 6.0 (and any Plone 6 minor release) still gets security support until the end of 2027.


## Highlights

Major changes since 6.0.15:

* Various security fixes:
  * Products.isurlinportal 2.1.0. See Plone security advisory 20260302.
  * plone.app.textfield 2.0.2 and plone.restapi 9.15.6. See Plone security advisory 20260605.
  * plone.app.contenttypes 3.0.12, plone.app.dexterity 3.2.3, plone.app.event 5.2.4, plone.app.portlets 5.0.8. See Plone security advisory 20260623. Plus for the same advisory: RestrictedPython 8.3 if you are on Python 3.10 or higher (it is incompatible with Python 3.9).
  * plone.restapi 9.15.7 (and optionally plone.autoform 2.0.5). See Plone security advisory 20260831.
  * plone.app.content 4.2.1, pip 26.2.2, certifi 2026.10.19. See Plone security advisory 20261022.
  * All fixes from Plone security fix 20261110: remote code execution.
    See [plone.org](https://plone.org/security/announcements/plone-security-advisory-20261110)
    or [community.plone.org](https://community.plone.org/t/plone-security-hotfix-20261110/23313).
* `twine`: Add compatibility with setuptools 77+.
  This fixes errors when making releases to PyPI: "twine.exceptions.InvalidDistribution: Metadata is missing required fields: Name, Version." .
* `plone.recipe.zope2instance`: Check for presence of Products.CMFPlone with multiple keys.  This is needed, depending on the used `zc.buildout` and `setuptools` versions.
* `plone.scale`:
  * Handle animated WebP images.
  * Add method to 'scale' SVGs by modifying display size and viewbox.
* `plone.namedfile`:
  * Add original image size url in the srcset generated in the srcset method.
  * Add default width and height attributes if none provided when using the srcset method.
  * "Scale" SVGs by setting the correct height and width for the given scale in its metadata.
  * Add a srcset method to the @@images view.
* `plone.app.content`: Alphabetically sort the list of portal types in the constraints configuration form.
* `plone.app.upgrade`: Add ``utils.remove_utility`` helper function.
* `plone.rest`: Add a `context` URL to exception responses.
  This can be used by a client to retrieve contextual data that may be needed to display the exception.
* `plone.restapi`:
  * Add support for the `RESTAPI_ADDITIONAL_NON_METADATA_ATTRIBUTES` environment variable, a comma-separated list of extra attribute names appended to the summary serializer's `non_metadata_attributes`.
  * Include all summary fields when serializing `next_item` and `previous_item`.
  * `@site` service: Add a way for add-ons to add additional data using an `ISiteEndpointExpander` adapter.
* `plone.staticresources`:
  * Upgrade mockup to 5.1.18 with dependency security fixes (DOMPurify, js-cookie, underscore, moment). See https://github.com/plone/mockup/releases/tag/5.1.18
* `plonetheme.barceloneta`: Support for required and invalid styles on form tabs.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.34.2](https://www.npmjs.com/package/@plone/volto/v/16.34.2).  See the [changelog](https://github.com/plone/volto/blob/16.34.2/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

Note that Volto 17, 18, and 19 are also available, and you can use them on Plone 6.0, but we will keep recommending Volto 16 by default.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.9, 3.10, 3.11, 3.12, and 3.13.

Using Python 3.8 will fail.
Note that meanwhile Python 3.9 and 3.10 are out of security support.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
packaging==25.0
pip==26.3; python_version > "3.9"
pip==26.0.1; python_version == "3.9"
setuptools==80.10.2
wheel==0.48.0
zc.buildout==4.2.0
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
