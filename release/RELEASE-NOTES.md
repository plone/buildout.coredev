# Release notes for Plone 6.1.0b2

* Released: December 19, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1.0b1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1.0b1/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1.0b1/constraints.txt](https://dist.plone.org/release/6.1.0b1/constraints.txt).
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1.0b1/versions.cfg](https://dist.plone.org/release/6.1.0b1/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1.0b1/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1.0b1/versions-ecosystem.cfg).


## Highlights

Major changes since 6.1.0b1:

* Supports Python 3.13.  Python 3.13.0 has a problem though, so you need at least 3.13.1.
* `Products.CMFPlone`: Allow bundles to be rendered after all others.  To render resources after all others, give them the "depends" value of "all".
* `Products.CMFEditions`: Fix ancient bug: "Can't pickle objects in acquisition wrappers" error in `OMOutsideChildrensModifier` and `OMInsideChildrensModifier`.
* `plone.app.event`: Provide an IContentListingObject adapter.
* `plone.app.multilingual`: use pat-contentbrowser as default widget for add translation form.
* `plone.distribution`: Fix bug where launch screen was blank in Chrome.
* `plone.namedfile`: Set `Link` header with `rel="canonical"` for file downloads. @mamico (#163)
* `plone.restapi`:
  * Fix log in after changing email when "email as login" is enabled.
  * When a Link content item is linked by UID, resolve its URL as the linked target URL for anonymous users.
* `plone.volto`:
  * Rename `default` distribution to `volto`.
  * Enable the `plone.versioning` behavior for the Page content type.
  * The `volto.head_title` behavior has been renamed to `volto.kicker`.  The old name still works, but is deprecated.  Content types should be updated to use the new name.
* `plonetheme.barceloneta`: Upgrade TinyMCE 7.6.0.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.4.0](https://www.npmjs.com/package/@plone/volto/v/18.4.0).  See the [changelog](https://github.com/plone/volto/blob/18.4.0/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This is the first Plone release to support Python 3.13.
This release supports Python 3.10, 3.11, 3.12, and 3.13.


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
