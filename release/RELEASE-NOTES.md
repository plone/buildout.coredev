# Release notes for Plone 6.1.0a4

* Released: August 1, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1.0a4/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1.0a4/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1.0a4/constraints.txt](https://dist.plone.org/release/6.1.0a4/constraints.txt), plus optionally [`constraints-extra.txt`](https://dist.plone.org/release/6.1.0a4/constraints-extra.txt) and [`constraints-ecosystem.txt`](https://dist.plone.org/release/6.1.0a4/constraints-ecosystem.txt).  Note: in 6.0 we did not have these last two files.  This may still change.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1.0a4/versions.cfg](https://dist.plone.org/release/6.1.0a4/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1.0a4/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1.0a4/versions-ecosystem.cfg).


## Highlights

Major changes since 6.1.0a3:

* `Products.CMFPlone`:
  * Use details element for collapsibles in the resource registry.  Makes it possible to toggle elements even with broken or missing javascript.
  * Remove queryCatalog and getFolderContents skins script.
  * Plone upgrade page: show error when upgrade is needed but no upgrades are available.  Especially show a note when the `plone.app.upgrade` package is not available.
  * Plone upgrade page: show list of previously installed packages that are currently missing.  For example: `plone.app.discussion` may be missing in Plone 6.1, unless you explicitly add it, or depend on the `Plone` package.
  * Remove `PropertiesTool` module and delete the `portal_properties` tool from the site in an upgrade step.
    This tool was deprecated and scheduled for removal in Plone 6.1.  If you use this tool in an add-on, you should move to storing settings in the `portal_registry` instead.
  * Remove `propertiestool` import step and usage of `portal_properties` and `site_properties`
  * Mockup TinyMCE settings: Remove deprecated AtD plugin settings.
* `plone.app.theming`: When calling the html serializer pass an encoding.  This is needed because we updated from `lxml` 4 to 5.
* `plone.app.iterate`: Remove old GenericSetup profile with id `plone.app.iterate`.  See [](https://github.com/plone/plone.app.iterate/issues/99#issuecomment-1484686642).
* Various packages: remove `portal_properties` code.
* `plone.base`:
  * Mockup TinyMCE settings: Remove deprecated AtD (After the Deadline spell checker) plugin settings and related views and interfaces.
  * Remove `ISearchSchemas` `types_not_searched` "Discussion Item" value to make `plone.app.discussion` a core addon.
    It is actually not needed anyway, also not part of the underlying vocabulary and would be lost on first save in control-panel.
* `plone.api`: Report if a permission does not exist when calling `api.user.has_permission`.
* `plone.restapi`:
  * Add cache rules for `@site` and `@navroot`.
  * Added `TeaserBlockSerializer` which updates the contents of a teaser block from its target if the block has `"overwrite": false`.
* `plone.app.content`: Speed improvement in `getVocabulary` for large vocabularies.
* `plonetheme.barceloneta`:
  * Add styles for details/summary based collapsibles.
  * Add support for labels wrapping input fields.
  * Add the portal_url parameter to be used with Diazo rules and implement it in `backend.xml`.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.0.0-alpha.42](https://www.npmjs.com/package/@plone/volto/v/18.0.0-alpha.42).  See the [changelog](https://github.com/plone/volto/blob/18.0.0-alpha.42/CHANGELOG.md).

Or use the latest Volto 17.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Docker

As we are still in the alpha stage, we are not yet creating `plone-backend` Docker images.


## Python compatibility

This release supports Python 3.10, 3.11, and 3.12.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==24.0
setuptools==69.5.1
wheel==0.43.0
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.
`setuptools` 70 will cause problems with current `zc.buildout` 3.0.1, so keep your eyes out for a new `zc.buildout` release.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
