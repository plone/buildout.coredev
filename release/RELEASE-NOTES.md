# Release notes for Plone 6.2.1 (unreleased)

* Last updated: June 23rd, 2026
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-62.html), explaining the biggest changes compared to 6.1.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2-dev/constraints.txt](https://dist.plone.org/release/6.2-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2-dev/versions.cfg](https://dist.plone.org/release/6.2-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes compared to 6.2.0:

* Add security fixes from June 5 and 23.  See:
  * https://community.plone.org/t/security-vulnerability-announcement-plone-app-textfield-and-plone-restapi/23050
  * https://community.plone.org/t/plone-security-fixes-20260623/23085
* `plone.namedfile`: Allow to set lazy to false, to suppress the `loading="lazy"` attribute.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.2 is meant to be used with Volto 19.
Latest release is [19.1.4](https://www.npmjs.com/package/@plone/volto/v/19.1.4).  See the [changelog](https://github.com/plone/volto/blob/19.1.4/packages/volto/CHANGELOG.md).  This is an alpha release, but it is ready to be made final.  Volto is just waiting for the Plone 6.2 final release.

Please have a look at the [upgrade guide](https://6.docs.plone.org/volto/upgrade-guide/index.html#upgrading-to-volto-19-x-x) for migration from Volto 18 to 19.

### Volto related changes in the Python backend since 6.2.0:

* nothing

## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.
It is being [renamed to Blicca](https://community.plone.org/t/say-hello-to-blicca-plone-classic-ui-has-a-new-name/23037).

### Classic UI related changes since 6.2.0:

* `plone.staticresources`: Update `mockup` from 5.6.4 to 5.6.6.  See also [`mockup` 5.6.6 changelog](https://github.com/plone/mockup/releases/tag/5.6.6) and earlier.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, 3.13, and 3.14.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
horse-with-no-namespace==20260202.0
pip==26.1.2
setuptools==81.0.0
wheel==0.47.0
zc.buildout==5.2.0
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
