# Release notes for Plone 6.0.14

* Released: December 19, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0.14/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0.14/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0.14/constraints.txt](https://dist.plone.org/release/6.0.14/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0.14/versions.cfg](https://dist.plone.org/release/6.0.14/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0.14/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0.14/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.13:

* Drop Python 3.8 support.
* Provisionally support Python 3.13.  It should work fine, but it has not been fully tested yet.
* `Products.CMFPlone`:
  * Allow bundles to be rendered after all others.  To render resources after all others, give them the "depends" value of "all".
  * Redirection control panel: Added support for start and end filters.
  * URL Management control panel: Find substring matches when querying aliases.
* `plone.app.event`: Provide an IContentListingObject adapter.
* `plone.namedfile`: Set `Link` header with `rel="canonical"` for file downloads.
* `plone.recipe.zope2instance`: Specify a standalone `logging.ini` configuration using the `wsgi-logging-ini-template` option in buildout.  The log configuration will be injected into `wsgi.ini` keeping all other default wsgi config.  The `wsgi-logging-ini-template` option cannot be used together with the `wsgi-ini-template`.
* `plone.restapi`:
  * Fix log in after changing email when "email as login" is enabled.
  * When a Link content item is linked by UID, resolve its URL as the linked target URL for anonymous users.
  * Added create and fetch aliases in CSV format.
  * Site service: Indicate whether the site supports filtering URL aliases by date.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.33.0](https://www.npmjs.com/package/@plone/volto/v/16.33.0).  See the [changelog](https://github.com/plone/volto/blob/16.33.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

Note that Volto 17 and 18 are also available, and you can use them on Plone 6.0, but we will keep recommending Volto 16 by default.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.9, 3.10, 3.11, and 3.12.
It drops Python 3.8 support.
It provisionally supports Python 3.13.  It should work fine, but it has not been fully tested yet.


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
