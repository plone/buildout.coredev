# Release notes for Plone 6.0.15 (unreleased)

* Last updated: February 24, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
* Canonical place for these [release notes](https://dist.plone.org/release/6.0-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.0-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.0-dev/constraints.txt](https://dist.plone.org/release/6.0-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.0-dev/versions.cfg](https://dist.plone.org/release/6.0-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.0-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.0-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

Major changes since 6.0.14:

* `plone.api`:
  * Added the content API helper function ``api.content.get_path``, which gets either the relative or absolute path of an object.
  * Added two new portal API functions:
    * ``api.portal.get_vocabulary``: Get a vocabulary by name.
    * ``api.portal.get_vocabulary_names``: Get a list of all available vocabulary names.
* `plone.app.users`: Email validation: use new registration tool method `principal_id_or_login_name_exists` if available.
  This helps in some corner cases when email-as-login is used.  This needs a new `Products.CMFPlone` release though.
* `plone.schema`: Fix email validation:
  * allow apostrophes
  * allow accented characters
  * allow ampersand in the user part
  * do not allow spaces.
  * accept TLDs with more than 4 characters
* `plone.restapi`:
  * Add a `@login` endpoint to get external login services' links.
  * In the `@registry` endpoint, added support for filtering the list of registry records.
  * Support working copies of the Plone Site.  But this feature can needs the new `plone.app.iterate` 6.1.0 release, which we won't add to Plone 6.0 for backwards compatibility reasons (removal of an old GenericSetup profile).  If you know what you are doing, you can add it.
* `plone.app.upgrade`: Ensure that the mimetypes registry globs contain valid patterns.
  If you have a site that started on Python 2.7 and is now running on Python 3.11, the mimetypes registry may give errors.  This upgrade step fixes it.
* `Products.MailHost`: Add support to `implicit_tls` flag. With this flag set, MailHost use TLS from the beginning of the connection, known as SMTPS and commonly used on TCP port 465.  You need to switch this on in the ZMI (Zope Management Interface).
* `zc.buildout`: Upgraded to the cleaned up version 4.  This has `packaging` as a dependency, and requires Python 3.9 or higher.
* `collective.recipe.omelette` (only relevant if you use Buildout):
  * No longer generate ``__init__.py`` files with namespace stanza in ``parts/omelette``.
    I think this was originally done to be able to go to ``parts/omelette``, start a standard Python, and be able to import everything.
    With current Python versions the ``__init__.py`` files are not needed for a directory to be importable.
  * Remove ``products`` recipe option and special handling of ``Products`` namespace.
    Zope 4 and higher no longer have the concept of a products directory.
    You can still use ``packages = path/to/products_dir Products`` if you need something similar.
  * Fix handling checkouts of native namespace packages.


## Volto frontend

The default frontend for new Plone 6 sites is Volto. Latest release is [16.33.0](https://www.npmjs.com/package/@plone/volto/v/16.33.0).  See the [changelog](https://github.com/plone/volto/blob/16.33.0/CHANGELOG.md).
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Also, existing Plone sites need some or more extensive changes to be upgraded before they can use the Volto Frontend. Please read the guide on [migrating from Plone Classic UI to Volto](https://6.docs.plone.org/backend/upgrading/version-specific-migration/migrate-to-volto.html).

Note that Volto 17 and 18 are also available, and you can use them on Plone 6.0, but we will keep recommending Volto 16 by default.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.  Support for Classic UI is especially relevant for existing Plone sites which for whatever reason or requirements are not yet ready to be upgraded to the Volto frontend.


## Python compatibility

This release supports Python 3.9, 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
packaging==24.2
pip==24.3.1
setuptools==75.6.0
wheel==0.45.1
zc.buildout==4.0
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that `zc.buildout` 4 has `packaging` as a dependency, so we added a pin for it in the requirements.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
