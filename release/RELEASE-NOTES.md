# Release notes for Plone 6.2.0a1 (2026-01-15)

* Last updated: January 15th, 2026
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-62.html), explaining the biggest changes compared to 6.1.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2.0a1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2.0a1/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2.0a1/constraints.txt](https://dist.plone.org/release/6.2.0a1/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2.0a1/versions.cfg](https://dist.plone.org/release/6.2.0a1/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2.0a1/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2.0a1/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Please test and help

This is the first alpha release of Plone 6.2.  We don't recommend this for production use, but please try it out in your projects.  You can report issues in the [`Products.CMFPlone` tracker](https://github.com/plone/Products.CMFPlone/issues/).

Please also test your add-ons on Plone 6.2.  If your package uses namespaces, we recommend that you switch to native namespaces.  This includes all packages in the `collective` namespace.  See the section "Move to native namespaces" in the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-62.html).  This should be considered a breaking change, so you should do this in a new major version of your add-on.  Still, as explained in the upgrade guide and below, it should work fine to use such a new major version in Plone 6.0 and 6.1.  But you may need to use `zc.buildout` 5 and/or install `horse-with-no-namespace` in your virtualenv.


## Highlights

These are the main changes compared to 6.1:

* We have switched to native namespaces (also known as implicit namespaces) for `plone.*`, `Products.*`, `collective.*` and all other namespaces.
* We use Zope 6.0b2, pinning versions with native namespaces.
* We have updated `zc.buildout` to version 5, and in the `requirements.txt` we have added `horse-with-no-namespace`.
  That helps avoid problems when not all packages in a namespace are using the same namespace style.
  See also below, in the section about "pip, buildout, setuptools".
* Some templates are being moved to `plone.app.layout`, this is ongoing.  Progress so far:
  * Moved lock info viewlet from `plone.locking`.
  * Modify `plone.protect.confirm` to use a simpler template that does not assume Classic UI is installed.
    The previous template was moved to `plone.app.layout`.
* `icalendar` has various breaking changes, but that should only affect you if you directly interact with that package.
* `plone.restapi`: `@aliases` service: Add support for filtering aliases for a non-root item.
* `Products.PluggableAuthService`: Add property to clear session data at login boundary to the session auth helper.  This property defaults to ``False`` to preserve the current behavior.  Clearing session data during login helps mitigate session fixation attacks: https://owasp.org/www-community/attacks/Session_fixation


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.2 is meant to be used with Volto 19.
Latest release is [19.0.0-alpha.21](https://www.npmjs.com/package/@plone/volto/v/19.0.0-alpha.21).  See the [changelog](https://github.com/plone/volto/blob/19.0.0-alpha.21/packages/volto/CHANGELOG.md).  This is an alpha release, but it is ready to be made final.  Volto is just waiting for the Plone 6.2 final release.

Please have a look at the [upgrade guide](https://6.docs.plone.org/volto/upgrade-guide/index.html#upgrading-to-volto-19-x-x) for migration from Volto 18 to 19.

### Key New Features in Volto 19

* Support for Subpath Domains (PLIP plone/volto#4290)
* Restore Unsaved Changes (PLIP plone/volto#4168)
* Improved Image Upload Widget (PLIP plone/volto#4268)

### General UI / Editor Improvements

* Cross-language support in the Blocks chooser search, improving block discovery on multilingual sites.
* Drag-and-drop file uploads directly into folder contents.
* New widgets: Size/Width/BlockAlignment
* Single-selection mode added to the SelectAutoComplete widget.

### Developer Tooling

* @plone/components library is now core, thus, it is allowed to be used in core
* Migration from Jest to Vitest as the default unit testing framework.
* Continued refactoring of core components towards modern React patterns (hooks and TypeScript).
* Internationalization and Accessibility
* Internationalised help text for selected fields (for example, Group Name).
* Improved screen-reader labels and more accessible button text across the UI.
* Improved toolbar accessibility and fixed several editor crashes.

### Breaking Changes and Important Upgrades

* Jest is no longer supported and removed from core
* The default language is now loaded from the backend API instead of being controlled via environment variables.
* Build tooling was forked (@plone/razzle and related Babel presets) to maintain long-term compatibility after upstream changes.
* Several widgets (such as AlignWidget and ButtonsWidget) were moved to @plone/components, which may require styling adjustments in custom projects.
* Updates to the Node.js toolchain, including dropping Node 20 support and now uses pnpm 10 with catalog support.
* Image handling changes require add-ons to use the Volto Image component instead of raw <img> tags.
* Related items (showRelatedItems) are now enabled by default.

### Bug Fixes and Quality Improvements

* Many miscellaneous bugfixes
* Multiple fixes to drag-and-drop interactions and folder contents behavior.
* Resolved login, redirect, and multilingual navigation issues.
* Increased stability of Cypress and other automated tests.
* Fixes related to server-side rendering hydration, image uploads, and schema handling.

### Volto related changes in the Python backend:

* `plone.volto`: Add larger scales to `plone.allowed_sizes` for new sites. This helps avoid the need to serve the original image which can be very large.
  * `2k` is large enough for a default-width image on a high-density display.
  * `4k` is large enough for a full-width images on high-density viewports up to 2000 pixels wide.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.

Classic UI related changes:

* `plone.base`:
  * `IClassicUISchema`: Add new control panel.
  * Add "license key" field to TinyMCE schema.
* `plone.app.layout`:
  * Add default GenericSetup profile with `IPloneAppLayout` BrowserLayer.
  * Add the new property `is_ajax` to the Plone layout view.
    This returns True, if an AJAX request is detected. This is done by checking if the `HTTP_X_REQUESTED_WITH` request header is set to `XMLHttpRequest`.
    `plone.app.theming` has related changes.
    Note: this is an unreliable way to detect AJAX requests. While many client-side
    libraries (like jQuery) add this request header automatically, the Fetch API
    does not. When using fetch, it is recommended to wrap it with a helper function
    that adds this header to each request.
* `plone.staticresources`: Update `mockup` from 5.4 to 5.5.1 with TinyMCE 8.  See also [`mockup` 5.5.1 changelog](https://github.com/plone/mockup/releases/tag/5.5.1).
* `plone.classicui`: Install the `plone.app.layout` default profile when creating a site using the classic distribution.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.

Support for Python 3.14 is expected in the next alpha or first beta release of 6.2.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
horse-with-no-namespace==20251105.1
packaging==25.0
pip==25.3
setuptools==80.9.0
wheel==0.45.1
zc.buildout==5.1.1
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

For more explanation, see the [`zc.buildout` 5 readme](https://pypi.org/project/zc.buildout/5.1.1/), the part about
"native namespaces and breaking changes in 5.x".  This is also good to read if you use pip instead of Buildout.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
