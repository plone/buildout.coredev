# Release notes for Plone 6.0.5 (unreleased)

* Updated: Tuesday May 23, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.4:

* `Zope`: Do not break on requests that pass both a query string and a `Content-Type` header or request body.
* `plone.app.caching`: Update the resourceRegistries ETag to use the config registry modification time.  This time is set since Plone 6.0.4.
* `plone.app.dexterity`: Content types control panel: Show behavior name and interface.
* `plone.app.z3cform`:
  * Merge utils and base classes from  `plone.app.widgets` and do not depend on it anymore.
  * Remove invalid unicode control characters for `TextareaWidget`.
* `plone.recipe.zeoserver`: Fix lost dependencies when defining additional `eggs` in buildout part.
* `plone.restapi`:
  * Add portal_type title (`type_title`) to content response
  * Added support for nested schemas with resolveuid deserializer
* `plone.staticresources`: Update `mockup` from 5.0.10 to 5.0.12:
  * pat markspeciallinks: Fix selector for tests.
  * pat recurrence: Fix default selected range option if there's no "repeat forever" button (which is default in the event behavior).
  * pat textareamimetypeselector: Async initialization of textareas. Fixes TinyMCE in modals not showing up (see Mosaic).
  * pat tinymce: Add urlconverter_callback and do not convert external links/images urls
  * pat tinymce: Do not remove current paragraph when inserting image.
* Several packages: Fix cyclic dependencies, drop Python 2 or Plone 5.2 support.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.20.6](https://www.npmjs.com/package/@plone/volto/v/16.20.6).  See the [changelog](https://github.com/plone/volto/blob/16.20.6/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available  and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==23.0.1
setuptools==67.6.1
wheel==0.40.0
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that `setuptools` 66 or higher is more strict with what versions it can recognize.  If you run `pip` or `buildout` and it suddenly cannot find a package with a non-standard version, then this may be the cause.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
