# Release notes for Plone 6.0.1

* Released: Tuesday January 31, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0.1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0.1/changelog.txt).

For technical wizards who want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0.1/constraints.txt](https://dist.plone.org/release/6.0.1/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0.1/versions.cfg](https://dist.plone.org/release/6.0.1/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0.1/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0.1/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.0:

* `Zope`:
  * Set the published default Content-Type header to text/plain if none has been set explicitly to prevent a cross-site scripting attack.  Also remove the old behavior of constructing an HTML page for published methods returning a two-item tuple.  This fix was already included in Plone 6.0.0.1 and 6.0.0.2.
  * Various other packages have fixes for this to avoid regressions.
* `plone.restapi`:
  * Internationalization of `@users` endpoint error messages.
  * Add pt_BR and fr translations.
* `plone.base`: Add missing TinyMCE plugin `autolink` to selectable plugins.
* `Products.CMFPlone`: When autologin after password reset is enabled (this is the default), use the same adapters as during normal login. Specifically: the `IInitialLogin` and `IRedirectAfterLogin` adapters.
* More Zope community packages have gotten official, tested Python 3.11 support.


## Volto frontend

The default frontend for Plone 6 is Volto. Latest release is [16.9.0](https://www.npmjs.com/package/@plone/volto/v/16.9.0).  See the [changelog](https://github.com/plone/volto/blob/16.9.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.
The Classic UI is still available when you only run the Python process.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
