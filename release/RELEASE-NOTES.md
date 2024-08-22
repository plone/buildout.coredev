# Release notes for Plone 6.1.0a5 (unreleased)

* Last updated: August 22, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1-dev/constraints.txt](https://dist.plone.org/release/6.1-dev/constraints.txt), plus optionally [`constraints-extra.txt`](https://dist.plone.org/release/6.1-dev/constraints-extra.txt) and [`constraints-ecosystem.txt`](https://dist.plone.org/release/6.1-dev/constraints-ecosystem.txt).  Note: in 6.0 we did not have these last two files.  This may still change.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1-dev/versions.cfg](https://dist.plone.org/release/6.1-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.1.0a4:

* `plone.app.content`:
  * `getVocabulary`: Fix for terms with incomplete HTML.
  * Fix `select_default_page` in VHM hosted sites.
* `Products.PortalTransforms`: Shortcut in safe_html: Check for signs of html or script, skip further processing if none are found.
* Newer `docutils` that works with Sphinx 8.
* `Products.validation`:
  * Moved to `versions-ecosystem.cfg`, and no longer test it in core, as core Plone is not using it.  It is used by the populare addon `collective.easyform`.
  * Drop support for Plone 5.2 and for Python 3.7 and lower.  Only Plone 6.0 and 6.1 are supported now.
  * Move translations from `plone.app.locales` to here.
* `Products.isurlinportal`: No longer patch `Products.CMFPlone`.  Instead, `Products.CMFPlone` will use us directly (it already does, but with a new `Products.CMFPlone` release it will do so more cleanly).  This solves cyclic dependencies.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.0.0-alpha.42](https://www.npmjs.com/package/@plone/volto/v/18.0.0-alpha.42).  See the [changelog](https://github.com/plone/volto/blob/18.0.0-alpha.42/CHANGELOG.md).

Or use the latest Volto 17.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Docker

As we are still in the alpha stage, we are not yet creating `plone-backend` Docker images.


## Python compatibility

This release supports Python 3.10, 3.11, and 3.12.


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
