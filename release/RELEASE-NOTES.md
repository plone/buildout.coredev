# Release notes for Plone 6.2.0a1 (unreleased)

* Last updated: November 26th, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* TODO Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.1.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2-dev/constraints.txt](https://dist.plone.org/release/6.2-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2-dev/versions.cfg](https://dist.plone.org/release/6.2-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes compared to 6.1:

* Some templates are being moved to `plone.app.layout`, this is ongoing.  Progress so far:
  * Moved lock info viewlet from `plone.locking`.
  * Modify `plone.protect.confirm` to use a simpler template that does not assume Classic UI is installed.
    The previous template was moved to `plone.app.layout`.
* We are in the middle of switching to native namespaces for `plone.*` and `Products.*`.
  We use alpha releases of dozens of plone packages now with native namespaces.
* We use Zope 6.0b1, pinning versions with native namespaces.
* We have updated `zc.buildout` to version 5, and in the `requirements.txt` we have added `horse-with-no-namespace`.
  That helps avoid problems when not all packages in a namespace are using the same namespace style.
  See also below, in the section about "pip, buildout, setuptools".
* `plone.protect`: We include 6.0.0a2, which is the first release of a `plone` namespace package that uses native namespaces.
* `plone.base`: `IClassicUISchema`: Add new control panel.
* `plone.app.layout`: Add the new property `is_ajax` to the Plone layout view.
  This returns True, if an AJAX request is detected. This is done by checking if the `HTTP_X_REQUESTED_WITH` request header is set to `XMLHttpRequest`.
  `plone.app.theming` has related changes.
  Note: this is an unreliable way to detect AJAX requests. While many client-side
  libraries (like jQuery) add this request header automatically, the Fetch API
  does not. When using fetch, it is recommended to wrap it with a helper function
  that adds this header to each request.
* `icalendar` has various breaking changes, but that should only affect you if you directly interact with that package.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.2 is meant to be used with Volto 18.
Latest release is [18.29.1](https://www.npmjs.com/package/@plone/volto/v/18.29.1).  See the [changelog](https://github.com/plone/volto/blob/18.29.1/packages/volto/CHANGELOG.md).
You can already test with the [latest Volto 19 alpha version](https://github.com/plone/volto/blob/main/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
horse-with-no-namespace==20251105.1
packaging==25.0
pip==25.3
setuptools==80.9.0
wheel==0.45.1
zc.buildout==5.1.0
```

In general you are free to use whatever versions work for you, but these worked for us.

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
