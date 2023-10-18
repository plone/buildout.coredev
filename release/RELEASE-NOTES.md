# Release notes for Plone 6.1-dev

* Last updated: Wednesday October 18, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1-dev/constraints.txt](https://dist.plone.org/release/6.1-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1-dev/versions.cfg](https://dist.plone.org/release/6.1-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.*:

* Some packages have become "core add-ons".  They are no longer a dependency of `Products.CMFPlone`, but of `Plone`:
  * `plone.app.multilingual`
* No longer let `Products.CMFPlone` depend on the deprecated `plone.app.widgets`.
  The package still exists, and can be used, but it only has backwards compatibility imports that get the real code from their new canonical places, mostly `plone.app.z3cform`.
  If your add-on uses this, you should explicitly depend on it.
  You are encouraged to update your import statements to the canonical places instead.  These should work on both Plone 6.0 and 6.1.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [17.2.0](https://www.npmjs.com/package/@plone/volto/v/17.2.0).  See the [changelog](https://github.com/plone/volto/blob/17.2.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.
There is preliminary support for Python 3.12.  This is pending a Zope release that officially supports this, and biggest blocker is a review of the `ResitrictedPython` package.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==23.2.1
setuptools==68.2.2
wheel==0.41.2
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
