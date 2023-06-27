# Release notes for Plone 6.0.6

* Released: Tuesday June 27, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0.6/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0.6/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0.6/constraints.txt](https://dist.plone.org/release/6.0.6/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0.6/versions.cfg](https://dist.plone.org/release/6.0.6/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0.6/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0.6/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.5:

* `plonetheme.barceloneta` and `plone.staticresources`: Update to Bootstrap 5.3 release.  Adopt colormode related variables from Bootstrap 5.3.
   You may need to update your custom themes.  See note below.
* `plone.restapi`: Added `@site` and `@navroot` endpoints.
* `plone.app.relationfield`: Removed unneeded dependency on plone.app.dexterity.
   This fixes a cyclic dependency: `plone.app.dexterity` depends on `plone.app.layout` which depends on `plone.app.relationfield`.
* `plone.app.locales`: updates for eu, es, pt_BR.
* `plone.volto`: Two bugfixes for migration from Classic UI to Volto:
   * Let the migration-form @@migrate_to_volto transform richtext to slate-blocks by default.
   * Fix value of unchecked checkboxes in migrate_to_volto.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.21.2](https://www.npmjs.com/package/@plone/volto/v/16.21.2).  See the [changelog](https://github.com/plone/volto/blob/16.21.2/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available  and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Updating custom themes

Now that Bootstrap 5.3 is available, you may need to update your custom theme for Classic UI.
This is *not* caused by Plone 6.0.6 moving to Bootstrap 5.3.
You could stay on Plone 6.0.5, and *still* have a problem with your custom theme, simply because Bootstrap 5.3 is available.

The problem is described in this [`bobtemplates.plone` issue](https://github.com/plone/plonetheme.barceloneta/issues/335).
Let's assume that a while ago you have followed the [theming training](https://training.plone.org/theming/preparation.html) to create a theme based on the standard Barceloneta theme.  All is working fine.
But now you want to have a fresh install, so you remove `node_modules` and `package-lock.json`.
You run `npm install`, still fine.
Then you run `npm run build` and get an error:

```
Error: Undefined variable.
   ╷
55 │     "primary": $primary-text-emphasis-dark,
```

The problem here is that you get Bootstrap 5.3, but your theme expects 5.2.
There are two ways to solve this.

If you want to keep using Bootstrap 5.2:

* Edit `package.json` and let the `dependencies` contain this: `"@plone/plonetheme-barceloneta-base": "~3.0.3"`.
  This version has a proper pin so you stay on Bootstrap 5.2.
* Run `rm -rf node_modules package-lock.json && npm install && npm run build`.
* If you want to create a new theme based on Bootstrap 5.2, make sure to use `bobtemplates.plone==6.2.7`.

If you are fine with upgrading to Bootstrap 5.3:

* Edit `package.json` and let the `dependencies` contain this: `"@plone/plonetheme-barceloneta-base": "~3.1.0"`.
* In `styles/theme.scss` add two imports in part 3:
  * After `variables.colors.plone` add this line: `@import "@plone/plonetheme-barceloneta-base/scss/variables.colors.dark.plone";`
  * After `bootstrap/scss/variables` add this line: `@import "bootstrap/scss/variables-dark";`
* Run `rm -rf node_modules package-lock.json && npm install && npm run build`.
* If you want to create a new theme based on Bootstrap 5.3, make sure to use `bobtemplates.plone>=6.3`.


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
