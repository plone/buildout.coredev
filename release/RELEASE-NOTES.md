# Release notes for Plone 6.1.5

* Released: June 25, 2026
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1.5/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1.5/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1.5/constraints.txt](https://dist.plone.org/release/6.1.5/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1.5/versions.cfg](https://dist.plone.org/release/6.1.5/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1.5/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1.5/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

This is the last maintenance release of the Plone 6.1 series.
With the release of Plone 6.2, Plone 6.1 is out of maintenance support.  You are encouraged to upgrade.
All Plone 6 minor versions (6.0, 6.1, 6.2) get security support until 2027-12-31, 5 years after Plone 6.0.0 was released.
If Plone 7 is not out by that time, security support will be extended.

These are the main changes since 6.1.4:

* Add security fixes from June 5 and 23.  See:
  * https://community.plone.org/t/security-vulnerability-announcement-plone-app-textfield-and-plone-restapi/23050
  * https://community.plone.org/t/plone-security-fixes-20260623/23085
* `Products.isurlinportal`: Prevent URLs that start with more than two slashes to be considered as URLs in portal.
  See [security advisory](https://github.com/plone/Products.isurlinportal/security/advisories/GHSA-43gx-6gv6-3jcp).
* `plone.app.content`: Alphabetically sort the list of portal types in the constraints configuration form.
* `plone.namedfile`: Add original image size url in the srcset generated in the srcset method.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.35.1](https://www.npmjs.com/package/@plone/volto/v/18.35.1).  See the [changelog](https://github.com/plone/volto/blob/18.35.1/packages/volto/CHANGELOG.md).
You can also use [Volto 19](https://github.com/plone/volto/blob/main/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
packaging==26.2
pip==26.1.2
setuptools==81.0.0
wheel==0.47.0
zc.buildout==4.2.0
```

In general you are free to use whatever versions work for you, but these worked for us.
Note that if you use Buildout and are on `setuptools` 80+, you need the latest `zc.buildout` 4.1.12.

If you use `zc.buildout`, you can also choose to upgrade to version 5.x.
That helps avoid problems when not all packages in a namespace are using the same namespace style.
When using either `zc.buildout` or `pip` (or `uv`) you can also choose to install the `horse-with-no-namespace` package.

For more explanation, see the [`zc.buildout` 5 readme](https://pypi.org/project/zc.buildout/5.0.0/), the part about
"native namespaces and breaking changes in 5.x".  This is also good to read if you use pip instead of Buildout.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
