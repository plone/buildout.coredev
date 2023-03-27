# Release notes for Plone 6.0.3

* Released: Monday March 27, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0.3/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0.3/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0.3/constraints.txt](https://dist.plone.org/release/6.0.3/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0.3/versions.cfg](https://dist.plone.org/release/6.0.3/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0.3/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0.3/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.2:

* `plone.base`: Move `getNavigationRoot` and `getNavigationRootObject` from `plone.app.layout` to `plone.base.navigationroot.get_navigation_root_object`.
  This is part of a general move of essential basic functions to the `plone.base` package.
  This is a prerequisite of further decoupling and cleanup of dependencies, so the core of Plone can become smaller.
  Backwards compatible imports are left in `plone.app.layout`, so add-on packages do not need to change anything.
* `Zope`: Replace `cgi.FieldStorage` by `multipart` avoiding the `cgi` module deprecated by Python 3.11.
  Mark binary converters with a true ``binary`` attribute.
  Fix encoding handling and ``:bytes`` converter.
  This affects the way Zope handles request data, but in core Plone no changes were needed, except in a few tests.
* `plone.restapi`:
  * Fix missing `Decimal` field deserializer.
  * Fix translation of the error message for a password that is too short while adding a user.
  * Provide slateTable block serializer/deserializer to properly convert URLs to uids.
* `plone.staticresources`: Upgrade Mockup to 5.0.6.  This introduces the `pat-checklist` pattern.
* `Products.CMFPlone`: Use the new ``pat-checklist`` for groupuser management, and fix userlisting batch/showAll in group membership template.
* `plone.app.locales`: Update translations for pt_BR.
* Various packages: drop support for older Python, Zope or Plone versions, declare dependencies better, fix deprecation warnings, cleanup code.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.18.0](https://www.npmjs.com/package/@plone/volto/v/16.18.0).  See the [changelog](https://github.com/plone/volto/blob/16.18.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

When you use containers, you need both `plone/plone-backend` and `plone/plone-frontend`.


## ClassicUI

The Classic UI is still available as an option, especially for existing sites.
When you use containers, you only need `plone/plone-backend`.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==22.3.1
setuptools==65.7.0
wheel==0.38.4
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, especially newer ones, but these worked for us.

Note that `setuptools` 66 is more strict with what versions it can recognize.  If you run `pip` or `buildout` and it suddenly cannot find a package with a non-standard version, then this may be the cause.  This is why we stayed at version 65 for this release.
This already needed a fix in `Products.GenericSetup` in the code that ordered upgrade steps.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
