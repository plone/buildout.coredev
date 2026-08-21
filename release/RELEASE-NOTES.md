# Release notes for Plone 6.2.2 (unreleased)

* Last updated: August 22th, 2026
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-62.html), explaining the biggest changes compared to 6.1.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2.1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2-dev/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2-dev/constraints.txt](https://dist.plone.org/release/6.2-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2-dev/versions.cfg](https://dist.plone.org/release/6.2-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2-dev/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

These are the main changes compared to 6.2.1:

* Zope 6.2: Disable XML-RPC request support by default. The protocol is rarely used and disabling it reduces the potential for abuse. Set `enable-xmlrpc` to on in the Zope configuration if you really need XML-RPC support.
  In older Plone and Zope versions, when using Buildout and `plone.recipe.zope2instance`, you can set `zope-conf-additional = enable-xmlrpc off` to disable XML-RPC.
* `plone.testing`: Explicitly enable XML-RPC in the ``WSGIServer`` layer.
  Otherwise all robot tests fail, because they actually use XML-RPC to communicate with the server.
* `plone.base`: Add `area` to default `valid_tags` so HTML image maps work out of the box.
* `plone.batching` and others: Move package metadata from `setup.py` to `pyproject.toml`.
  This will happen to most Plone packages in the near future.  You should not notice any difference in practice.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.2 is meant to be used with Volto 19.
Latest release is [19.3.0](https://www.npmjs.com/package/@plone/volto/v/19.3.0).  See the [changelog](https://github.com/plone/volto/blob/19.3.0/packages/volto/CHANGELOG.md).

Please have a look at the [upgrade guide](https://6.docs.plone.org/volto/upgrade-guide/index.html#upgrading-to-volto-19-x-x) for migration from Volto 18 to 19.

### Volto related changes in the Python backend since 6.2.1:

* nothing

## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.  Our documentation now refers to this frontend as 'Classic UI'.
It is being [renamed to Blicca](https://community.plone.org/t/say-hello-to-blicca-plone-classic-ui-has-a-new-name/23037).

### Classic UI related changes since 6.2.1:

* `plone.staticresources`: Update `mockup` from 5.6.7 to 5.6.8.  See also [`mockup` 5.6.8 changelog](https://github.com/plone/mockup/releases/tag/5.6.8).
* `plonetheme.barceloneta`: `barceloneta-toolbar.css`: Scope CSS declarations.
  Scope the CSS for the `barceloneta-toolbar.css` file, so that its styles do not pollute the rest of the site.
  This way you can use `barceloneta-toolbar.css` in a site without Bootstrap or with a Bootstrap version other than 5 without breaking your site's design.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, 3.13, and 3.14.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
horse-with-no-namespace==20260202.0
pip==26.2.1
setuptools==81.0.0
wheel==0.47.0
zc.buildout==5.2.0
```

In general you are free to use whatever versions work for you, but these worked for us.
If you don't use buildout, it should be fine to use `setuptools` 82+.

You can also try `zc.buildout` 6.0.0a1.
This includes its own copy of the deprecated `pkg_resources` module, so it works with the latest `setuptools` version.
And it fixes support for PEP 660 develop packages, so `pyproject.toml` only, made with `setuptools` or with newer build systems like `hatchling`, `flit`, `pdm`.
See the [major changes](https://pypi.org/project/zc.buildout/6.0.0a1/#user-content-major-changes-in-6-x) for details information.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
