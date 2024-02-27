# Release notes for Plone 6.1.0a2

* Last updated: Tuesday February 27, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
  Yes, we need to start on a 6.1 upgrade guide.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1.0a2/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1.0a2/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1.0a2/constraints.txt](https://dist.plone.org/release/6.1.0a2/constraints.txt), plus optionally [`constraints-extra.txt`](https://dist.plone.org/release/6.1.0a2/constraints-extra.txt) and [`constraints-ecosystem.txt`](https://dist.plone.org/release/6.1.0a2/constraints-ecosystem.txt).  Note: in 6.0 we did not have these last two files.  This may still change.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1.0a2/versions.cfg](https://dist.plone.org/release/6.1.0a2/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1.0a2/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1.0a2/versions-ecosystem.cfg).


## Highlights

Major changes since 6.1.0a1:

* `plone.api`: Implemented unrestricted find of content types.
* `plone.app.multilingual`: Implement a more reasonable default for "connect translations" dialog.
* `plone.volto`: Add `VOLTO_FRONTEND_DOMAIN` as env var for `volto.frontend_domain` registry setting.
* `plone.app.caching`: Fix purging of image scale paths for Dexterity content.
* `plone.app.content`: Fix escaping HTML in ``tags`` popover and in vocabulary items.
* `plone.app.z3cform`:  Implement missing PasswordWidget adapter.  Now the login form is using a proper password input field again.
* `plone.restapi`: Give Site Administrator permission to manage users.
  To make this possible, we now check the "plone.app.controlpanel.UsersAndGroups" permission instead of "cmf.ManagePortal" in a lot of operations in the users and groups endpoints.
* `Products.CMFPlone`: Remove volatile cached resource viewlet content to fix context aware expressions.
* Fix various icon paths.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [17.15.2](https://www.npmjs.com/package/@plone/volto/v/17.15.2).  See the [changelog](https://github.com/plone/volto/blob/17.15.2/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, 3.11, and 3.12.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==23.3.2
setuptools==69.0.3
wheel==0.42.0
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
