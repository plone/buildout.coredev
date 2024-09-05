# Release notes for Plone 6.1.0a5

* Released: September 5, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1.0a5/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1.0a5/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1.0a5/constraints.txt](https://dist.plone.org/release/6.1.0a5/constraints.txt), plus optionally [`constraints-extra.txt`](https://dist.plone.org/release/6.1.0a5/constraints-extra.txt) and [`constraints-ecosystem.txt`](https://dist.plone.org/release/6.1.0a5/constraints-ecosystem.txt).  Note: in 6.0 we did not have these last two files.  This may still change.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1.0a5/versions.cfg](https://dist.plone.org/release/6.1.0a5/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1.0a5/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1.0a5/versions-ecosystem.cfg).


## Highlights

The main change in this release is that Discussion is a core add-on.
Discussion is a feature that allows your site visitors to comment on web pages for any content object. The code behind this is in the `plone.app.discussion` package. In Plone 6.0 and earlier, this was a dependency of `Products.CMFPlone`, making it available for installation in all Plone sites. In Plone 6.1 it's a dependency of the `Plone` package.

See the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html#discussion-is-a-core-add-on) on how to handle this if your site has comments and you want to keep them.

The following packages are involved in the changes:

* `plone.app.discussion`: Move this package in the space of Plone Core add-ons.
  It now depends on `Products.CMFPlone` and is no longer installed by default.
  It is still available in the default `Plone` distribution, but can be omitted in customizations.
  Installing this in the Add-ons control panel will enable comments globally.
* `Products.CMFPlone`: Remove dependency on `plone.app.discussion`.
* `plone.app.contenttypes`: Do not enable the `plone.allowdiscussion` behavior by default.
* `plone.app.dexterity`: Move `plone.discussion` behavior out of this package to `plone.app.discussion`.
* `plone.app.upgrade`: Cleanup `plone.app.discussion` settings when the package is not available.  If the site contains comments, we throw an error and stop the upgrade.  The advice then is to add the `plone.app.discussion` package.

Other major changes since 6.1.0a4:

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
* `zc.buildout`: update to version that works with latest setuptools.
* `plone.app.locales:
  * Remove `Products.validation` translations. They are moved to that package.
  * Update es, pt-br, eu, cn, and nl translations.
* `Products.CMFPlone`:
  * Use `five.registerPackage` so an editable install with `pip` works.
  * Use `Products.isurlinportal` directly, instead of relying on it patching our `URLTool`.  This solves a cyclic dependency.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.0.0-alpha.42](https://www.npmjs.com/package/@plone/volto/v/18.0.0-alpha.42).  See the [changelog](https://github.com/plone/volto/blob/18.0.0-alpha.42/packages/volto/CHANGELOG.md).

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
pip==24.2
setuptools==74.0.0
wheel==0.44.0
zc.buildout==3.1.0
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
