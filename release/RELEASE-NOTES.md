# Release notes for Plone 6.0.15 (unreleased)

* Last updated: January 30, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.14:

* Fully support Python 3.13.  In the previous release it worked fine, but it had not been fully tested yet.
  Note that 3.13.0 does not work: you need at least 3.13.1.
* Fixed lots of deprecation warnings in lots of packages.
* `plone.restapi`:
  * Add a `@login` endpoint to get external login services' links.
  * In the `@registry` endpoint, added support for filtering the list of registry records.
* `Products.PlonePAS`: Return an error when trying to access the PAS views from the web.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.33.0](https://www.npmjs.com/package/@plone/volto/v/16.33.0).  See the [changelog](https://github.com/plone/volto/blob/16.33.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

Note that Volto 17 and 18 are also available, and you can use them on Plone 6.0, but we will keep recommending Volto 16 by default.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.9, 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==24.3.1
setuptools==75.6.0
wheel==0.45.1
zc.buildout==3.3
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that there is also a [`zc.buildout` 4.0.0a1](https://pypi.org/project/zc.buildout/4.0.0a1/) release that you could try.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
