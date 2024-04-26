# Release notes for Plone 6.1-dev

* Last updated: Friday April 26, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/upgrade/index.html), explaining the biggest changes compared to 5.2.
  Yes, we need to start on a 6.1 upgrade guide.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1-dev/constraints.txt](https://dist.plone.org/release/6.1-dev/constraints.txt), plus optionally [`constraints-extra.txt`](https://dist.plone.org/release/6.1-dev/constraints-extra.txt) and [`constraints-ecosystem.txt`](https://dist.plone.org/release/6.1-dev/constraints-ecosystem.txt).  Note: in 6.0 we did not have these last two files.  This may still change.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1-dev/versions.cfg](https://dist.plone.org/release/6.1-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.1.0a2:

* This release drops support for Python 3.8 and 3.9.  We only support Python 3.10, 3.11, and 3.12.
* `plone.staticresources`: Upgrade to TinyMCE 7 without any breaking changes in core Plone.  If you have custom TinyMCE plugins, please check with https://www.tiny.cloud/docs/tinymce/latest/migration-from-6x/ if you need to upgrade your code.
* `plonetheme.barceloneta`:
  * TinyMCE 7.0.  This is a version bump only. There are no CSS changes from TinyMCE 6 -> 7.
  * Remove deprecated SVG font resources

The rest of the changes are the same as for Plone 6.0.11, released yesterday, as there is still a lot of overlap between these versions:

* `mxdev`: Fix for Python 3.12 virtual envs.
* `plone.namedfile`, `plone.formwidget.namedfile` and `plone.app.z3cform`: Support for allowed media types.
  Support to constrain files to specific media types with an "accept" attribute on file and image fields, just like the "accept" attribute of the HTML file input.  With this, allowed file types are checked already before uploading, while still also being checked on the server side.
* `plone.app.z3cform`: Use `label_css_class` attribute from widget if available in checkbox_input and radio_input.
* `plone.namedfile`: Improve contenttype detection logic for unregistered but common types.  Change `get_contenttype` to support common types which are or were not registered with IANA, like `image/webp` or `audio/midi`.
* `plone.app.discussion`: Provide HCaptcha if `plone.formwidget.hcaptcha` is installed.
* `plone.base`: Make the TinyMCE `help` and `accordion` plugins available as options.
  To really use this, you need an add-on, like [`collective.outputfilters.tinymceaccordion`](https://github.com/collective/collective.outputfilters.tinymceaccordion).  But at least the options are available now.
* `plone.base` and `plone.app.layout`: Add a field ``webstats_head_js`` to the Site controlpanel and render its contents in the head section using `IHtmlHeadLinks` viewlet manager.  Reason: some javascript needs to be loaded at the bottom of the page, and some in the head section.
* `plone.recipe.zope2instance`: Add support for setting `max_value_length` in Sentry init.  When you use this option, you should use `sentry-sdk` 1.29.0 or higher.
* `plone.restapi`: Add available languages information and the site timezone to the `@site` endpoint.
* `lxml`: Upgraded from version 4.9.4 to 5.2.1.  This could mean small differences in html.  See the [changelog](https://github.com/lxml/lxml/blob/lxml-5.2.1/CHANGES.txt).  If you get wrong results, maybe because Diazo theming rules are parsed differently, it should be fine to downgrade, but version 4 is not maintained anymore.
* `Products.PortalTransforms`: Use `Cleaner` from new package `lxml_html_clean`.
  This was factored out from `lxml` in version 5.2.0.  See https://lxml-html-clean.readthedocs.io/


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Latest release is [17.15.5](https://www.npmjs.com/package/@plone/volto/v/17.15.5).  See the [changelog](https://github.com/plone/volto/blob/17.15.5/CHANGELOG.md).
You can also try Volto 18.0.0-alpha.28.  Most likely, the first final release of Plone 6.1 will use Volto 18.


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


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
