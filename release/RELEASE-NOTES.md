# Release notes for Plone 6.2.3

* Released: November 10th, 2026
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-62.html), explaining the biggest changes compared to 6.1.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2.3/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2.3/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2.3/constraints.txt](https://dist.plone.org/release/6.2.3/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2.3/versions.cfg](https://dist.plone.org/release/6.2.3/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2.3/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2.3/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes compared to 6.2.2.1:

* All fixes from Plone security fix 20261110: remote code execution.
  See [plone.org](https://plone.org/security/announcements/plone-security-advisory-20261110)
  or [community.plone.org](https://community.plone.org/t/plone-security-hotfix-20261110/23313).
* `plone.exportimport`:
  * Add `--path` and `--paths` options to `plone-exporter` to export only parts of a site. Relations, translations, discussions, portlets and redirects are limited to the exported content.
  * Enable browser layers when importing/exporting content.
* `plone.app.querystring`:
  * Allow sorting query results by location (``path``), which orders items by their full physical path.
  * Add the ``plone.app.querystring.operation.string.currentUID`` ("Current item") operation, which filters an index by the UID of the item where the query runs. Add-ons can enable it on fields for their own relation indexes.
* `plone.restapi`:
  * Controlpanel service: Added `description`, `group_id`, and `icon` to the control panels listed by `GET @controlpanels`, taken from their configlets.
  * Add support for `multipart/form-data` in POST and PATCH requests, allowing file uploads alongside JSON metadata.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.2 is meant to be used with Volto 19.
Latest release is [19.7.0](https://www.npmjs.com/package/@plone/volto/v/19.7.0).  See the [changelog](https://github.com/plone/volto/blob/19.7.0/packages/volto/CHANGELOG.md).

Please have a look at the [upgrade guide](https://6.docs.plone.org/volto/upgrade-guide/index.html#upgrading-to-volto-19-x-x) for migration from Volto 18 to 19.


### Volto related changes in the Python backend since 6.2.2:

* plone.volto: Add `personal_tools` actions (Profile, Preferences and Site Setup) for the Volto toolbar's Personal tools menu, with an upgrade step for existing sites.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.
It is being [renamed to Blicca](https://community.plone.org/t/say-hello-to-blicca-plone-classic-ui-has-a-new-name/23037).

### Classic UI related changes since 6.2.2:

* `plone.staticresources`: Update `mockup` from 5.6.10 to 5.6.15 (TinyMCE 8.9.3 security fix, Patternslib 9.11.1, Svelte 5.57.3).
  See also [`mockup` 5.6.15 changelog](https://github.com/plone/mockup/releases/tag/5.6.15) and earlier.
* `plonetheme.barceloneta`: `barceloneta-toolbar.css`: Scope CSS declarations.
  Scope the CSS for the `barceloneta-toolbar.css` file, so that its styles do not pollute the rest of the site.
  This way you can use `barceloneta-toolbar.css` in a site without Bootstrap or with a Bootstrap version other than 5 without breaking your site's design.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, 3.13, and 3.14.

Note: we will soon drop support for Python 3.10, as this is out of security support.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
horse-with-no-namespace==20260202.0
pip==26.3
setuptools==84.2.1
wheel==0.48.0
zc.buildout==6.0.2
```

In general you are free to use whatever versions work for you, but these worked for us.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
