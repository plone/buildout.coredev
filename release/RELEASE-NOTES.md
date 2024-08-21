# Release notes for Plone 6.0.13 (unreleased)

* Last updated: August 21, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0.12/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0.12/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0.12/constraints.txt](https://dist.plone.org/release/6.0.12/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0.12/versions.cfg](https://dist.plone.org/release/6.0.12/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0.12/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0.12/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.12:

* `plone.app.content`:
  * `getVocabulary`: Fix for terms with incomplete HTML.
  * Fix `select_default_page` in VHM hosted sites.
* `Products.PortalTransforms`: Shortcut in safe_html: Check for signs of html or script, skip further processing if none are found.
* Newer `docutils` that works with Sphinx 8.
* `Products.validation`:
  * Drop support for Plone 5.2 and for Python 3.7 and lower.  Only Plone 6.0 and 6.1 are supported now.  Note that this is not used by core Plone, but for example by `collective.easyform`.
  * Move translations from plone.app.locales to here.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.31.11](https://www.npmjs.com/package/@plone/volto/v/16.31.11).  See the [changelog](https://github.com/plone/volto/blob/16.31.11/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

Note that Volto 17 is also available, and you can use it on Plone 6.0, but we will keep recommending Volto 16 by default.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, 3.11, and 3.12.

Note that Plone 6.0 is tested on Python 3.8 and 3.11 on every change to core packages.  For the other Python versions we run the tests once a week.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==24.0
setuptools==69.5.1
wheel==0.43.0
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.
`setuptools` 70 will cause problems with current `zc.buildout` 3.0.1, so keep your eyes out for a new `zc.buildout` release.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
