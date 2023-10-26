# Release notes for Plone 6.0.8rc1

* Last updated: Friday October 27, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.0.7:

* `plone.scale`: Keep scaled WEBP images in WEBP format instead of converting to JPEG.
* `plone.recipe.zope2instance`: Add `dos_protection` config.  See "Error when uploading large files" below.
* `Zope`:
  * Make sure the object title in the ZMI breadcrumbs is quoted to prevent a cross-site scripting issue.
  * Base the inline/attachment logic developed for CVE-2023-42458 on the media type proper (ignore parameters and whitespace and normalize to lowercase).
* `plone.base`: Move interface `INameFromTitle` from `plone.app.content` here.
  This helps avoiding a circular dependency between `plone.app.dexterity` and `plone.app.content`.
* `plone.app.querystring`: Add a way to specify a context for getting vocabularies in the QuerystringRegistryReader.
  See [PR 137](https://github.com/plone/plone.app.querystring/pull/137).


## Error when uploading large files

With Zope 5.8.4+ (included in Plone 6.0.7) you may get `zExceptions.BadRequest: data exceeds memory limit` when uploading an image or file of more than 1 MB.  This is at least true when you have `plone.restapi` installed, which is the case if you use the default frontend (Volto).
You have various ways to increase this limit.

If you use Buildout, you can add this in your instance/zeoclient recipe, and choose your own limit:

```
zope-conf-additional =
    <dos_protection>
      form-memory-limit 4MB
    </dos_protection>
```

If you used [`cookiecutter-zope-instance`](https://github.com/plone/cookiecutter-zope-instance) to create a Plone site, you can add these lines to `etc/zope.conf`, just like the latest development version [offers](https://github.com/plone/cookiecutter-zope-instance/pull/12/files):

```
<dos_protection>
  form-memory-limit 4MB
</dos_protection>
```

Of course you are free to choose a higher or lower limit.



## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.25.0](https://www.npmjs.com/package/@plone/volto/v/16.25.0).  See the [changelog](https://github.com/plone/volto/blob/16.25.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

Note that Volto 17 is also available, and you can use it on Plone 6.0, but we will keep recommending Volto 16 by default.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.

There is preliminary support for Python 3.12, but this is not officially recommended yet.  Especially some changes in `RestrictedPython` may need to happen still.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==23.3.1
setuptools==68.2.2
wheel==0.41.2
zc.buildout==3.0.1
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
