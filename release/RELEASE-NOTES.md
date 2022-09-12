# Release notes for Plone 6.0.0b2

Released: Saturday September 10, 2022.

## Highlights

Most important change is that this release officially **drops Python 3.7 support**.
Currently everything still work in 3.7, all tests pass, but beta 2 is the last release where this is the case.
See discussion in [this issue](https://github.com/plone/Products.CMFPlone/issues/3635) and especially [this community poll](https://community.plone.org/t/plone-6-0-drop-support-for-python-3-7-and-3-8/15549).

Python 3.8, 3.9 and 3.10 are supported.  Python 3.11 support will likely be added after the final release.  Most work for this is being done in the Zope packages.  Note that Plone add-ons may choose to support less Python versions, especially dropping 3.8.  You are encouraged to **use Python 3.10**, which is also the fastest supported Python.

Other major changes since 6.0.0b2:

* `plone.session`:

  * Creating per-user keyrings in order to have session invalidation on log-out (server-side logout).
  * Cookie attribute SameSite is set to "Lax".

* `plone.restapi`:

  * Add `@portrait` endpoint.
  * Add support for importing profiles in `@addons` endpoint.
  * Add support to search for fullname, email, id on the `@users` endpoint with `"?search="`.

* `plone.volto`:

  * Added preview image link behavior.
  * Use slate as default text block in default contents for ``default-homepage`` and
  ``multilingual`` profile.

* `plone.app.z3cform`:

  * Add `default_time` attribute/argument to Date- and DatetimeWidget to allow the converter to set a custom time when nothing was given.
  * Customizable DateWidget formatter length.

* `plone.i18n`:

  * Add some more native names to language-country combinations
  * Fix the missing native names for language-country variants.

* `plone.app.robotframework`: Add keyword 'Wait For Elements'.  Here the requested element is allowed to match multiple times.


## Volto frontend

The default frontend for Plone 6 is Volto. Latest release is [16.0.0-alpha.30](https://www.npmjs.com/package/@plone/volto/v/16.0.0-alpha.30).
See the [changelog](https://github.com/plone/volto/blob/16.0.0-alpha.30/CHANGELOG.md).


## Python compatibility

This release supports Python 3.8, 3.9, and 3.10.
As said, technically 3.7 still works, but it is not supported anymore.


## Installation

For installation instructions, see the [documentation](https://6.dev-docs.plone.org/install/index.html).
This documentation is under development, but this should get you up and running.  No worries.
