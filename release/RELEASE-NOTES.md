# Release notes for Plone 6.0.0b3

Released: Tuesday October 4, 2022.

## Highlights

Major changes since 6.0.0b2:

* `Products.PlonePAS`: Increase the minimum password length to 8 characters.

* `pip`: We have actually *downgraded* `pip` because version 22.2 and higher have an incompatibility with Buildout.  Buildout works, but it cannot read the information about which Python versions are required for a package.  If you do not use Buildout, feel free to use the latest `pip` version.

* `plone.restapi`:

  * Add `@userschema` endpoint for getting the user schema.

  * Add `@transactions` endpoint to fetch transactions that have been made through the Plone website.

  * Added `@aliases` endpoint with GET/POST/DELETE.

  * Improve performance of serializing image scales.

* `TinyMCE` rich text editor updates in various packages:

  * Disable `advlist` plugin by default, it produces unclean inline styles.

  * Add `inserttable` to toolbar.

  * Add and improve table styles.

  * Add UI styles in non-inline mode.

  * Actually load theme-specified styles CSS in TinyMCE.

* `plone.staticresources`:

  * Use successor repository of `svg-country-flags`.

  * Upgrade to Bootstrap 5.2.2.

  * Upgrade to Mockup 5.0.0-alpha.24.

* `plonetheme.barceloneta`:

  * Bootstrap 5.2.2

* `plone.app.layout`: Use a variable to allow customization of the image scale used for social tags


## Volto frontend

The default frontend for Plone 6 is Volto. Latest release is [16.0.0-alpha.40](https://www.npmjs.com/package/@plone/volto/v/16.0.0-alpha.40).
See the [changelog](https://github.com/plone/volto/blob/16.0.0-alpha.40/CHANGELOG.md).


## Python compatibility

This release supports Python 3.8, 3.9, and 3.10.


## Installation

For installation instructions, see the [documentation](https://6.dev-docs.plone.org/install/index.html).
This documentation is under development, but this should get you up and running.  No worries.
