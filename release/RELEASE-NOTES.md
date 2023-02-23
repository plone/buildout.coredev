# Release notes for Plone 6.0.2rc1

* Released: Thursday February 23, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

For technical wizards who want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.1:

* `plone.rest`: Change the HTTP status from 301 (Moved Permanently) to 302 (Found) for GET requests and to 307 (Temporary Redirect) for other request methods.  This fixes problems when an existing redirect is re-used.
* `plone.restapi`:
  * Request of own user data provides joined groups.
  * Implement `IPurgePaths` for RestAPI traversal (`++api++`).
  * Implement `IRuleAction` and `IRuleCondition` schema serialization in `@controlpanels/content-rules/` endpoint.
* `plone.staticresources`: Upgrade Mockup to 5.0.5.
* `plone.app.locales`: Update translations for tr, es, eu, de.
* Various packages: drop support for older Python, Zope or Plone versions, declare dependencies better, cleanup code.


## Volto frontend

The default frontend for Plone 6 is Volto. Latest release is [16.11.0](https://www.npmjs.com/package/@plone/volto/v/16.11.0).  See the [changelog](https://github.com/plone/volto/blob/16.11.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.
The Classic UI is still available when you only run the Python process.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
