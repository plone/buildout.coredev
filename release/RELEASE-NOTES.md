# Release notes for Plone 6.1.0rc1 (unreleased)

* Last updated: January 29, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1-dev/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1-dev/constraints.txt](https://dist.plone.org/release/6.1-dev/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1-dev/versions.cfg](https://dist.plone.org/release/6.1-dev/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1-dev/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1-dev/versions-ecosystem.cfg).


## Highlights

Major changes since 6.1.0b2:

* Fixed lots of deprecation warnings in lots of packages.
* `icalendar`: Upgraded to version 6.  This has support for the `zoneinfo` Python standard library.
  Plone is not ready for that yet, so in `plone.app.event`, which uses it for the ical/vcal downloads, we configure it to keep using the `pytz` library as before.
  You should not notice a difference, but if you have own code that uses `icalendar`, you should look at the [breaking changes in v6.0.0a0](https://github.com/collective/icalendar/blob/v6.0.0a0/CHANGES.rst).
* `plone.exportimport` and `plone.distribution` have changes that make the exported files more "stable": when you create a site with a distribution and then make a fresh export, there should be no changes in the distribution.
  * Include revisions only when passing `--include-revisions` in `bin/plone-exporter` and `bin/export-distribution`.
  * Export principals: sort groups, roles, and members.
  * Import: update modification dates again at the end. The original modification dates may have changed.
  * Do not export parent info.
    This information is no longer needed: during import, parents are now always found by path and not by UID.
    From now on, the import ignores any parent info that is set.
* `plone.restapi`:
  * Add a `@login` endpoint to get external login services' links.
  * In the `@registry` endpoint, added support for filtering the list of registry records.
* `plone.volto`: Implement a specific robots.txt for Volto sites.
  The existing standard one would [block API calls made by Google](https://github.com/plone/plone.volto/issues/178).
  There is an upgrade step which will update the existing `plone.robots_txt` registry setting unless it has been customized.
* `Products.PlonePAS`: Return an error when trying to access the PAS views from the web.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.7.0](https://www.npmjs.com/package/@plone/volto/v/18.7.0).  See the [changelog](https://github.com/plone/volto/blob/18.7.0/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
pip==24.3.1
setuptools==75.6.0
wheel==0.45.1
zc.buildout==3.3
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that there is also a [`zc.buildout` 4.0.0a1](https://pypi.org/project/zc.buildout/4.0.0a1/) release that you could try.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
