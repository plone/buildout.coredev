# Release notes for Plone 6.2.0a1 (unreleased)

* Last updated: February 27, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* TODO Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2-dev/constraints.txt](https://dist.plone.org/release/6.2-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2-dev/versions.cfg](https://dist.plone.org/release/6.2-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes since 6.1.0:

* `five.intid`, `five.customerize`, `five.localsitemanager`: Drop support for `pkg_resources` namespace and replace it with PEP 420 native namespace.
* `trove-classifiers`: Added "Framework :: Plone :: 6.2" classifier for use in PyPI classifiers.
* `collective.recipe.omelette` (only relevant if you use Buildout):
  * No longer generate ``__init__.py`` files with namespace stanza in ``parts/omelette``.
    I think this was originally done to be able to go to ``parts/omelette``, start a standard Python, and be able to import everything.
    With current Python versions the ``__init__.py`` files are not needed for a directory to be importable.
  * Remove ``products`` recipe option and special handling of ``Products`` namespace.
    Zope 4 and higher no longer have the concept of a products directory.
    You can still use ``packages = path/to/products_dir Products`` if you need something similar.
  * Fix handling checkouts of native namespace packages.
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
* `plone.staticresources`: Update to latest `mockup`.  This improves the new content browser widget (used for uploading images or selecting content).
* `plone.autoinclude`: Fix importing module when the module name differs from the project name.  This can easily happen with `setuptools` 75.8.1, though maybe 75.8.2 fixes it in some cases.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.2 is meant to be used with Volto 18.
Latest release is [18.8.1](https://www.npmjs.com/package/@plone/volto/v/18.8.1).  See the [changelog](https://github.com/plone/volto/blob/18.8.1/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


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


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
