# Release notes for Plone 6.0.4

* Updated: Monday April 24, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0.4/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0.4/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0.4/constraints.txt](https://dist.plone.org/release/6.0.4/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0.4/versions.cfg](https://dist.plone.org/release/6.0.4/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0.4/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0.4/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.3:

* `plone.app.event` and `plone.app.multilingual`: Breaking dependency cleanup: move declaration of language independence of IEventBasic fields from `plone.app.event` to `plone.app.multilingual`.
* `plone.app.locales`: Updated translations for `es` and `eu`.
* `plone.base`: Check for container field / attribute when trying to create content with same id.
* `plone.restapi`:
  * Apply a cache ruleset to the `/@querystring-search` endpoint.
  * Add `UID` to `relationvalue_converter` summary.
  * Add `querystring_search` `GET` method.
* `plone.schema`:
  * Introduce extras `plone.schema[supermodel]` and `plone.schema[schemaeditor]`.
  * The package now works in its vanilla installation as an addon for z3c.form, without any other plone dependencies.
* `plone.staticresources`: Update to `mockup` 5.0.10. Fixes `pat-recurrence` UI issues.
* `Products.CMFPlone`:
  * Add a last modification time to the resource registry.
    We update this when changing anything related: when changing the resource registry in its control panel or activating an add-on.
    This avoids needing a restart before seeing changes when you run in production mode.
  * Mockup TinyMCE settings: Fix URLs in TinyMCE `external_plugins` settings.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.20.4](https://www.npmjs.com/package/@plone/volto/v/16.20.4).  See the [changelog](https://github.com/plone/volto/blob/16.20.4/CHANGELOG.md).
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
