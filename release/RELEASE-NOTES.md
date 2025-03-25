# Release notes for Plone 6.1.1

* Released: March 25, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1.1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1.1/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1.1/constraints.txt](https://dist.plone.org/release/6.1.1/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1.1/versions.cfg](https://dist.plone.org/release/6.1.1/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1.1/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1.1/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes since 6.1.0:

* Lots of packages: Replace `pkg_resources` with `importlib.metadata`/`importlib.resources`.  See the "Distribution not found" section below for why this is important.
* `Zope`:
  * Add configuration switch to turn off the built-in XML-RPC support.
    Hardly anyone needs XML-RPC, and it can lead to strange errors when you get malicious and/or spam requests.
  * Add configuration switch for the maximum allowed number of form fields.
    `multipart` version 1.2.1 introduced a default value of 128, Zope now
    sets it to 1024.
* `plone.recipe.zope2instance`: Support for new Zope option `enable-xmlrpc`.
  Usage: `zope-conf-additional = enable-xmlrpc off`.
  **Setting this is recommended for most sites.**
* `plone.autoinclude`:
  * If a distribution is not found, try to normalize the name like recent setuptools is doing and try again.
  * Fix importing module when the module name differs from the project name.
    This can easily happen with ``setuptools`` 75.8.1, though 75.8.2 fixes most of it.
* `Products.CMFPlone`:
  * RegistrationTool: add method `principal_id_or_login_name_exists`.
    This is factored out from the `isMemberIdAllowed` method, which now calls this after checking the allowed member id pattern.
  * Fix moving portal actions between categories.
  * Use contentbrowser options for TinyMCE image/link browser.  This also fixes the `basePath` calculation for uploading.
* `collective.recipe.omelette` (only relevant if you use Buildout):
  * No longer generate `__init__.py` files with namespace stanza in `parts/omelette`.
    I think this was originally done to be able to go to `parts/omelette`, start a standard Python, and be able to import everything.
    With current Python versions the `__init__.py` files are not needed for a directory to be importable.
  * Remove `products` recipe option and special handling of `Products` namespace.
    Zope 4 and higher no longer have the concept of a products directory.
    You can still use `packages = path/to/products_dir Products` if you need something similar.
  * Fix handling checkouts of native namespace packages.
* `plone.api`:
  * Added the content API helper function `api.content.get_path`, which gets either the relative or absolute path of an object.
  * Added two new portal API functions:
    * `api.portal.get_vocabulary`: Get a vocabulary by name.
    * `api.portal.get_vocabulary_names`: Get a list of all available vocabulary names.
  * Add the `api.content.iter_ancestors` function for iterating over an object acquisition chain.
  * Implement `plone.api.addon` module.
* `plone.app.users`: Email validation: use new registration tool method `principal_id_or_login_name_exists` if available.
  This helps in some corner cases when email-as-login is used.  The method is in the new `Products.CMFPlone` release.
* `plone.schema`: Fix email validation:
  * allow apostrophes
  * allow accented characters
  * allow ampersand in the user part
  * do not allow spaces.
  * accept TLDs with more than 4 characters
* `plone.staticresources`: Update to latest `mockup`.  This improves the new content browser widget (used for uploading images or selecting content).
* `plone.app.caching`:
  * Trigger purge on workflow change.
  * Fix purging for deleted content.
* `plone.exportimport`:
  * Report object creation during import using the `plone-importer` cli. Use `--quiet` to disable it.
  * Do not stop the import if an object parent is missing.
* `plone.restapi`:
  * Apply block serialization and deserialization transforms also to JSON fields.
    This includes converting internal URLs to resolveuid URLs.
  * Add a new endpoint, `@inherit`, for getting values from behaviors inherited from ancestors in the object hierarchy.
  * Add a `@userschema/registration` endpoint to get the fields for the registration form.
  * Added `multilingual` feature to `@site` endpoint.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.10.1](https://www.npmjs.com/package/@plone/volto/v/18.10.1).  See the [changelog](https://github.com/plone/volto/blob/18.10.1/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
packaging==24.2
pip==25.0.1
setuptools==75.8.2
wheel==0.45.1
zc.buildout==4.1.4
```

In general you are free to use whatever versions work for you, but these worked for us.


## Distribution not found

On February 25, `setuptools` 75.8.1 was released.  This had an innocent sounding change: "Fix wheel file naming to follow binary distribution specification."  The consequences were large.  Any namespace packages that are released using this or a later version, have a slightly different "binary wheel" name, for example `plone_autoinclude-2.0.2.whl` with an underscore instead of `plone.autoinclude-2.0.2.whl` with a dot.  Result is that you can easily get a "distribution not found" error when starting Plone, or even during install.

This new Plone 6.1.1 should fix all problems.  If you run into problems with this Plone version or an older one, the following observations may help.

* `setuptools` 75.8.2 fixes some of the problems: it tries to find a distribution by multiple names, for example `plone.autoinclude`, `plone-autoinclude`, `plone_autoinclude`.  So use this version or a higher one.
* Buildout had more problems than pip, but that should be fixed with `zc.buildout` 4.1.4.
* In pip-based projects I had more problems on Python 3.9 than on newer versions.  (Plone 6.1 cannot use 3.9, so no problem there.)  I had slightly more problems on 3.13 than on 3.11 and 3.12.  So if all else fails, switching the Python version may help.
* `plone.autoinclude` was the package that needed the most changes, because this uses entry points and here we quickly ran into problems in finding a distribution.  Latest 2.0.3 has all the fixes that we found necessary.  It needs Python 3.9 minimum.
* A lot of Plone packages where using the `pkg_resources` part of `setuptools` to check for the existence of a distribution, or do other tasks related to Python packages.  This is deprecated, and can mostly be replaced by switching to `importlib.metadata`, which is a library available in standard Python since version 3.8.  We made the switch for most packages.  See [`CMFPlone` issue 4126](https://github.com/plone/Products.CMFPlone/issues/4126) for a big list of packages with changes.  This also contains examples of changes that needed to be made.
* You may be using add-ons or have own code that uses `pkg_resources`.  You should probably replace that, getting inspiration from the previous link.  You can leave `declare_namespace` lines untouched; that is something for another time.
* If you have a namespace package that you want to support in projects that cannot switch to the latest `setuptools` or `zc.buildout` (which both require Python 3.9 minimum), you can restrict which `setuptools` version is used while building the binary wheel.  You need as maximum 75.8.0.  We did this for `plone.restapi` and `plone.autoinclude`.  To do this, the package needs a `pyproject.toml` file with contents like this:

```
[build-system]
requires = ["setuptools>=68.2,<=75.8.0"]
```

or this:

```
[build-system]
requires = ["setuptools==75.8.0"]
```

This needs `zest.releaser` 9.5.0, if you are using this for releasing your packages to PyPI.  See its [changelog](https://github.com/zestsoftware/zest.releaser/blob/9.5.0/CHANGES.rst) for this and other recent changes, also relates to the new `setuptools` versions.

Note that on March 19, `setuptools` 77 was released with initial support for so called "license expressions" ([PEP 639](https://peps.python.org/pep-0639/#add-license-expression-field)).  This gave errors when I tried making releases to PyPI: "twine.exceptions.InvalidDistribution: Metadata is missing required fields: Name, Version." . So this may need some changes in `setup.py/cfg` or `pyproject.toml`.  So if you try to upload to PyPI and get a similar error, you may indeed want to restrict the setuptools version to something less than 77.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
