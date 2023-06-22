# Release notes for Plone 6.0.6rc1

* Last updated: Thursday June 22, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.5:

* `plonetheme.barceloneta` and `plone.staticresources`: Update to Bootstrap 5.3 release.  Adopt colormode related variables from Bootstrap 5.3.
   See note below: Must update custom themes.
* `plone.restapi`: Added `@site` and `@navroot` endpoints.
* `plone.app.relationfield`: Removed unneeded dependency on plone.app.dexterity.
   This fixes a cyclic dependency: `plone.app.dexterity` depends on `plone.app.layout` which depends on `plone.app.relationfield`.
* `plone.app.locales`: updates for eu, es, pt_BR.
* `plone.volto`: Two bugfixes for migration from Classic UI to Volto:
   * Let the migration-form @@migrate_to_volto transform richtext to slate-blocks by default.
   * Fix value of unchecked checkboxes in migrate_to_volto.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.21.0](https://www.npmjs.com/package/@plone/volto/v/16.21.0).  See the [changelog](https://github.com/plone/volto/blob/16.21.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available  and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Must update custom themes

You may need to update your custom theme.
See https://github.com/plone/bobtemplates.plone/pull/550#issuecomment-1594445727
TODO: add that inline in these release notes.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==23.1.2
setuptools==67.8.0
wheel==0.40.0
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that `setuptools` 66 or higher is more strict with what versions it can recognize.  If you run `pip` or `buildout` and it suddenly cannot find a package with a non-standard version, then this may be the cause.

When you install Plone with `pip` on Python 3.11, you may want to set environment variable `_PIP_USE_IMPORTLIB_METADATA=0`.
This can give a large performance increase when reinstalling packages.
Or wait on a new pip version with a fix.
See [pip issue 12079](https://github.com/pypa/pip/issues/12079).


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
