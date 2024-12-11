# Release notes for Plone 6.1.0b2 (unreleased)

* Last updated: December 11, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1.0b1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1.0b1/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1.0b1/constraints.txt](https://dist.plone.org/release/6.1.0b1/constraints.txt), plus optionally [`constraints-extra.txt`](https://dist.plone.org/release/6.1.0b1/constraints-extra.txt) and [`constraints-ecosystem.txt`](https://dist.plone.org/release/6.1.0b1/constraints-ecosystem.txt).  Note: in 6.0 we did not have these last two files.  This may still change.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1.0b1/versions.cfg](https://dist.plone.org/release/6.1.0b1/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1.0b1/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1.0b1/versions-ecosystem.cfg).


## Highlights

Major changes since 6.1.0b1:

* `Products.CMFEditions`: Fix ancient bug: "Can't pickle objects in acquisition wrappers" error in `OMOutsideChildrensModifier` and `OMInsideChildrensModifier`.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.0.0](https://www.npmjs.com/package/@plone/volto/v/18.0.0).  See the [changelog](https://github.com/plone/volto/blob/18.0.0/packages/volto/CHANGELOG.md).  You saw that right: this is no longer an alpha release, but a final release!

Or use the latest Volto 17.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Docker

In the alpha stage, we did not create any [`plone-backend` Docker images](https://hub.docker.com/r/plone/plone-backend), but for the first beta we did.  You can now use the `plone/plone-backend:6.1.0b1` image.

## Python compatibility

This release supports Python 3.10, 3.11, and 3.12.

The underlying Zope 5.11 supports Python 3.13, but this Plone release not yet.  We should be close though.

## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==24.2
setuptools==75.2.0
wheel==0.44.0
zc.buildout==3.3
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that there is also a [`zc.buildout` 4.0.0a1](https://pypi.org/project/zc.buildout/4.0.0a1/) release that you could try.

## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
