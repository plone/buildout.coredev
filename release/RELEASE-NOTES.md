# Release notes for Plone 6.0.rc1

* Released: Thursday December 14 6, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.8:

* `Zope`: Officially support Python 3.12.
* `plone.restapi`:
  - Added preview_image and preview_image_link to the list of smart fields for resolveuid and link integrity.
* ZEO:
  - Version 6.0.0 supports Python 3.12.
  - It also switches "to using `async/await` directly instead of `@coroutine/yield`".
  - That last change sounds like it could potentially have unforeseen side effects, so it would be good to get this more field tested.
    (I may be too cautious here.)
  - So for Python 3.11 and lower we pin 5.4.1, and on Python 3.12 we pin 6.0.0.
    You are encouraged to try out the newer version on all Python versions, and report any problems.
    We will likely pin the new version for all Python versions in the next Ploen bugfix release.
  - See the [ZEO 6.0.0 changelog](https://github.com/zopefoundation/ZEO/blob/6.0.0/CHANGES.rst)

## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.26.0](https://www.npmjs.com/package/@plone/volto/v/16.26.0).  See the [changelog](https://github.com/plone/volto/blob/16.26.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

Note that Volto 17 is also available, and you can use it on Plone 6.0, but we will keep recommending Volto 16 by default.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.

There is preliminary support for Python 3.12, but this is not officially recommended yet.  Especially some changes in `RestrictedPython` may need to happen still.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==23.3.1
setuptools==69.0.2
wheel==0.42.0
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
