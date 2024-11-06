# Release notes for Plone 6.1.0b1

* Released: October 31, 2024
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1.0b1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1.0b1/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1.0b1/constraints.txt](https://dist.plone.org/release/6.1.0b1/constraints.txt), plus optionally [`constraints-extra.txt`](https://dist.plone.org/release/6.1.0b1/constraints-extra.txt) and [`constraints-ecosystem.txt`](https://dist.plone.org/release/6.1.0b1/constraints-ecosystem.txt).  Note: in 6.0 we did not have these last two files.  This may still change.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1.0b1/versions.cfg](https://dist.plone.org/release/6.1.0b1/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1.0b1/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1.0b1/versions-ecosystem.cfg).


## Highlights

The main change in this release is the support and inclusion of Plone Distributions.
A Plone distribution is a Python package that defines specific features, themes, add-ons, and configurations that get activated when creating a Plone site.
Now it is available in core Plone as the recommended way for creating a new Plone site.

The documentation explains the [concept of distributions](https://6.docs.plone.org/conceptual-guides/distributions.html), how to [create a distribution](https://6.docs.plone.org/developer-guide/create-a-distribution.html) and what you may need to [do when upgrading](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html#distributions).

The following packages are involved in the changes.  Their links already give an idea of how to create and use distributions:

* [`plone.distribution`](https://github.com/plone/plone.distribution) provides the framework for defining distributions.
* [`plone.exportimport`](https://github.com/plone/plone.exportimport) imports and exports content, users, and other objects between Plone sites.
  `plone.distribution` uses it.
* [`plone.volto`](https://github.com/plone/plone.volto) is the distribution to create a Plone site with the default frontend, Volto.
* [`plone.classicui`](https://github.com/plone/plone.classicui) is the distribution to create a Plone site with the Classic UI frontend.
* `Plone`: Add dependency on `plone.classicui` distribution.
  `plone.volto` was already a dependency.  Both pull in `plone.distribution` and `plone.exportimport` as dependencies.
* `Products.CMFPlone` has the following related changes:
  * Only register the add site form and root Zope overview if `plone.distribution` is not available.
  * Remove advanced options from Add Plone Site form.
    If you need more options, you should add a Plone Distribution to your packages.
    The main ones are `plone.volto` and `plone.classicui`.
    We now only create a basic Plone site without default example content.
  * `factory.addPloneSite`: remove `setup_content` and `content_profile_id` keyword arguments.
    We no longer load default content. Use a Plone Distribution if you need this.
    Or pass an extra profile id in the `extension_ids` keyword argument.
  * You can pass a `distribution_name` to `factory.addPloneSite`.
    We then pass all other arguments and keyword arguments to the `plone.distribution` site api.

Other major changes since 6.1.0a5:

* `plone.app.caching`:
  * Replace `plone.app.caching` import step with a post handler.
  * Removed the `plone.app.caching.txt` Generic Setup flag file that was needed by the import step.
  * Add uninstall profile.
* `plone.staticresources`:
  * New `pat-contentbrowser` pattern from `mockup==5.2.0-alpha.11`. See https://github.com/plone/mockup/releases/tag/5.2.0-alpha.11 for details.
  * Update to latest `mockup=5.2.0-beta.0`. See https://github.com/plone/mockup/releases/tag/5.2.0-beta.0
* `plone.app.z3cform`: Implement new `ContentBrowserWidget` for `pat-contentbrowser` pattern.
  The deprecated `RelatedItemsWidget` and `pat-relateditems` pattern is still available
  and imports should not break. But the default widget and converter adapter registration for
  z3c.relationfield is changed to the new widget.
* `plone.app.relationfield`: Use new `ContentBrowserWidget` with `pat-contentbrowser` support.
* `plone.volto`:
  * Drop support for Plone 5.2 and Plone 6.0.
  * The following GenericSetup profiles were removed: `default-homepage`, `default-homepage-drafjs`, `default-homepage-slate`, `demo` and `richtext`.
* `Products.CMFPlone` and several other packages have robot tests: functional tests that use a real browser.
  Most of these were ported to playwright based tests, using the robotframework browser library.
  This should result in more stable tests that are easier to write and maintain.
* `Products.CMFPlone`: URL Management (Redirection) control panel:
  * Added support for start and end filters.
  * Find substring matches when querying aliases.
* `plone.recipe.zope2instance`: Specify a standalone `logging.ini` configuration using the `wsgi-logging-ini-template` option in buildout.
  The log configuration will be injected into `wsgi.ini` keeping all other default wsgi config.
  The `wsgi-logging-ini-template` option cannot be used together with the `wsgi-ini-template`.
* `plone.restapi`:
  * Added create and fetch aliases in CSV format.
  * Site service: Indicate whether the site supports filtering URL aliases by date.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.0.0](https://www.npmjs.com/package/@plone/volto/v/18.0.0).  See the [changelog](https://github.com/plone/volto/blob/18.0.0/packages/volto/CHANGELOG.md).  You saw that right: this is no longer an alpha release, but a final release!

Or use the latest Volto 17.


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Docker

In the alpha stage, we did not create any `plone-backend` Docker images.
This is expected to change now that we have a first beta release.


## Python compatibility

This release supports Python 3.10, 3.11, and 3.12.

The underlying Zope 5.11 supports Python 3.13, but this Plone release not yet.  We should be close though.

## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==24.2
setuptools==75.2.0
wheel==0.44.0
zc.buildout==3.3
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that there is also a [`zc.buildout` 4.0.0a1](https://pypi.org/project/zc.buildout/4.0.0a1/) release that you could try.

## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
