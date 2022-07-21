# Release notes for Plone 6.0.0-dev

Last updated: Friday July 22, 2022.

## Highlights

Major changes since 6.0.0a6:

* `Products.CMFPlone`:
  * Removed our expressions patch. This was a patch to avoid some too strict checks by `Zope` / `Products.PageTemplates`. But in Plone 6 it should be fine to be stricter. The ``STRICT_TRAVERSE_CHECK`` environment variable is no longer read.
  * Initially open accordions in resource registry. Hide via JS when no errors occur. This makes it possible to fix a breaking error.
  * Resource bundle dependency on multiple comma separated names.
* `plone.dexterity`: Remove long deprecated imports and fallbacks.
* `plonetheme.barceloneta`: Update to Bootstrap 5.2.0 (released this week).


## Volto frontend

The default frontend for Plone 6 is Volto. Latest release is [16.0.0-alpha.15](https://www.npmjs.com/package/@plone/volto/v/16.0.0-alpha.15).
This contains the much anticipated integration of the `volto-state` editor.  See the [changelog](https://github.com/plone/volto/blob/master/CHANGELOG.md).


## Python compatibility

This release supports Python 3.7, 3.8, 3.9, and 3.10.
Support for Python 3.10 is still a bit provisional, as our testing infrastructure needs some updates before we can fully test this.
But your friendly Plone Release Manager is using Python 3.10 for local development, so it should be okay.


## Installation

For installation instructions, see the [documentation](https://6.dev-docs.plone.org/install/index.html).
This documentation is under development, but this should get you up and running.  No worries.
