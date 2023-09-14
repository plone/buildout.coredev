# Release notes for Plone 6.0.7rc1

* Last updated: Thursday September 14, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.6:

* `Zope`: Security fixes in `AccessControl` and `RestrictedPython`.  See [community announcement](https://community.plone.org/t/zope-4-8-9-and-5-8-4-released-with-a-security-fix/17849).
* `plone.namedfile`:
  * Add internal modification timestamp with fallback to _p_mtime.
  * Use new internal modification timestamp as part of the hash key for scales.
* `plone.app.widgets`: Make this package deprecated. It still works, and is included in Plone 6.0, but Plone 6.1 will not ship with it.
  Widget base classes have been moved to ``plone.app.z3cform.widgets.patterns``.
  Also see ``plone.app.widgets.utils`` for information about moving utility methods to their new location.
* `plone.app.robotframework`: Add support for `playwright`-based tests via `robotframework-browser`.
* `plone.app.z3cform`: Introduce new Email-Widget which is used for `plone.schema.email.IEmail` fields.  It uses the input type `email`.
* `plone.volto`: Add `block_types` index to zcatalog. By default it is only added for new Plone sites.
  To add it to an existing site, run `plone.volto.upgrades.add_block_types_index` manually.
* `plone.app.multilingual`: Fixes for Indonesian in a multilingual site.  Fix `set_recursive_language` to actually find child objects.
* `plone.app.querystring`: Fix the `currentUser`` operation when the current user's username is different from their user id.
* `plone.namedfile`: Fixed issue with SVG images that contain extensive metadata.
* `plone.staticresources`: update to Mockup 5.1.4:
  * pat structure: Fix popover-structure-columns, use 2-column layout. (9fb499e)
  * pat structure: Fix sticky position when toolbar is on top.
  * pat tinymce: Fix image modal with selected image.
* `plonetheme.barceloneta`: Update Bootstrap to `5.3.1`
* `Products.CMFCore`:
  * Improve handling of PortalFolder filter input.
  * Provide a way to not publish items that are acquired.
* `plone.restapi`:
  * Allow passing additional parameters to the delete users endpoint to request not to delete local roles and memberareas.
  * When serializing blocks, `image_scales` is now added to blocks that contain a resolveuid-based `url`.
  * When deserializing blocks, `image_scales` is removed.
  * Add `visit_blocks` util for finding all nested blocks.
* `plone.app.locales`: Updates to nl translations.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.24.0](https://www.npmjs.com/package/@plone/volto/v/16.24.0).  See the [changelog](https://github.com/plone/volto/blob/16.24.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==23.2
setuptools==68.0.0
wheel==0.40.0
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that `setuptools` 66 or higher is more strict with what versions it can recognize.  If you run `pip` or `buildout` and it suddenly cannot find a package with a non-standard version, then this may be the cause.
And  `setuptools` 68.1.0 until at least 68.1.2 may give problems with namespace packages, especially when they have multiple levels, like `plone.app.*`, and are installed in editable mode.  And pinning a specific version of `setuptools` in your virtual environment may not even be enough for this case.  See https://github.com/plone/meta/issues/172


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
