# Release notes for Plone 6.1.3 (unreleased)

* Last updated: October 1st, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1-dev/constraints.txt](https://dist.plone.org/release/6.1-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1-dev/versions.cfg](https://dist.plone.org/release/6.1-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes since 6.1.2:

* `plone.app.iterate`: Add working copy support for `LRF` type (Language Root Folder).
* `plone.app.multilingual`: Add `plone.locking` behavior to `LRF` type. This is required for the working copy to work in `LRF`.
* `plone.exportimport`:
  * Support export/import of user `login_name`.
  * Support non-root PloneSite import/export.
* `plone.rest`: Add a `context` URL to exception responses.
  This can be used by a client to retrieve contextual data that may be needed to display the exception.
* `plone.app.vocabularies`: Now in CatalogVocabulary getTerm raises LookupError when it cannot find the referred object instead of returning None.
* `plone.base`: Cleanup `TinyMCESchema.plugins` to the actual existing plugins.
* `plonetheme.barceloneta`: Update to Bootstrap 5.3.8.
* Internal change in lots of packages: Move distribution to src layout.

## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.27.3](https://www.npmjs.com/package/@plone/volto/v/18.27.3).  See the [changelog](https://github.com/plone/volto/blob/18.27.3/packages/volto/CHANGELOG.md).
You can already test with the [latest Volto 19 alpha version](https://github.com/plone/volto/blob/main/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
packaging==25.0
pip==25.2
setuptools==80.9.0
wheel==0.45.1
zc.buildout==4.1.12
```

In general you are free to use whatever versions work for you, but these worked for us.
Note that if you use Buildout and are on `setuptools` 80+, you need the latest `zc.buildout` 4.1.12.

If you use `zc.buildout`, you can also choose to upgrade to version 5.x, currently in alpha release.
That helps avoid problems when not all packages in a namespace are using the same namespace style.
When using either `zc.buildout` or `pip` (or `uv`) you can also choose to install the `horse-with-no-namespace` package.
Plone 6.2 (under development) already uses both.

Let's explain why you may want to do this.
Problems start when you have multiple packages in the same namespace, that use different namespace implementations.
Then on startup of Plone you may get an error saying "Package not found".
This depends on what you use to install the packages.
In the following examples, we have two packages in the same namespace, say `ns.native` (using native namespaces) and `ns.deprecated` (using pkg_resources style).

* Make editable installs of both packages (`pip install -e` or in buildout, `develop =`):

  - This works neither in pip nor in buildout.
  - You can install the [`horse-with-no-namespace`](https://pypi.org/project/horse-with-no-namespace/) package to get this working.

* Make a normal install of both packages:

  - This works fine in pip.
  - This fails in buildout 4.x.
  - This works fine in buildout 5.x.

* Make a normal install of one package and an editable install of the other:

  - This works fine in pip.
  - This fails in buildout 4.x.
  - This fails in buildout 5.x as well.  But again, you can use `horse-with-no-namespace` to get this working.

For more explanation, see the [`zc.buildout` 5 readme](https://pypi.org/project/zc.buildout/5.0.0a3/), the part about
"native namespaces and breaking changes in 5.x".  This is also good to read if you use pip instead of Buildout.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
