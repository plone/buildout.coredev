# Release notes for Plone 6.0.10rc1

* Released: Thursday February 22, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.9:

* Plone 6.0.10 is the first release that officially supports Python 3.12.
* `plone.api`: Implemented unrestricted find of content: `api.content.find(unrestricted=True)`
* `plone.restapi`:
  * Translate validation error messages in the deserializer.
  * Give Site Administrator permission to manage users. To make this possible, we now check the "plone.app.controlpanel.UsersAndGroups" permission instead of "cmf.ManagePortal" in a lot of operations in the users and groups endpoints.
* `plone.volto`: Add `VOLTO_FRONTEND_DOMAIN` as env var for `volto.frontend_domain` registry setting.
* `plone.app.caching`: Fix purging of image scale paths for Dexterity content.
* `plone.app.content`: Fix escaping HTML in ``tags`` popover and in vocabulary items.
* `plone.app.theming`: Traverse to theme resources from the portal. This fixes a broken theme when rendering accessible content contained in an inaccessible navigation root.
* `plone.staticresources`: Update dependencies: mockup 5.1.9, bootstrap 5.3.3, bootstrap-icons 1.11.3.
* `Products.CMFPlone`:
  * Remove volatile cached resource viewlet content to fix context aware expressions.
  * Add `data-bundle="diazo"` back, for backward compatibility with backend.xml (Classic UI).
  * Add a `data-bundle="plonecustomcss"` also for `@@custom.css` stylesheet


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.30.3](https://www.npmjs.com/package/@plone/volto/v/16.30.3).  See the [changelog](https://github.com/plone/volto/blob/16.30.3/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

Note that Volto 17 is also available, and you can use it on Plone 6.0, but we will keep recommending Volto 16 by default.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, 3.11, and 3.12.

Plone 6.0.10 is the first release that officially supports Python 3.12.

Note that Plone 6.0 is tested on Python 3.8 and 3.11 on every change to core packages.  For the other Python versions we run the tests once a week.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==24.0
setuptools==69.0.3
wheel==0.42.0
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
