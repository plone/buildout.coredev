# Release notes for Plone 5.2.15

* Released: Thursday August 1, 2024
* This is expected to be the last maintenance release.  Already one more than was promised.
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://5.docs.plone.org/manage/upgrading/version_specific_migration/upgrade_to_52.html), explaining the biggest changes compared to 5.1.
* Canonical place for these [release notes](https://dist.plone.org/release/5.2.15/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/5.2.15/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/5.2.15/constraints.txt](https://dist.plone.org/release/5.2.15/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/5.2.15/versions.cfg](https://dist.plone.org/release/5.2.15/versions.cfg).


## Highlights

Major changes since 5.2.14:

* `plone.recipe.zope2instance`:
  * Add support for setting max_value_length in Sentry init.  When you use this option, you should use `sentry-sdk` 1.29.0 or higher.
  * Add ``dos_protection`` config.  With Zope 5.8.4+ you may get ``zExceptions.BadRequest: data exceeds memory limit`` when uploading an image or file of more than 1 MB.  To increase this limit, you can add this in your instance recipe, and choose your own limit: `zope-conf-additional = <dos_protection>form-memory-limit 4MB</dos_protection>`
* `plone.app.discussion`: Provide HCaptcha if `plone.formwidget.hcaptcha` is installed.  Apply validation for all captchas.
* `plone.restapi`: Added `@site` and `@navroot` endpoints.
* For the rest see the full packages changelog linked above.


## Last maintenance release

Plone 5.2.15 is planned to be the last regular release of Plone 5.2.

Plone 5.2 is actually already out of maintenance support since October 2023, but I decided it was fine to gather some last changes and release them.

There is still security support, but only until October 31, 2024.
At that moment, even Python 3.8 is out of security support by the Python community.


## Python compatibility

This release supports Python 2.7 and 3.8.

Python 3.6 and 3.7 should still work, but these are end-of-life, untested, and no longer supported.

Plone 5.2 still supports Python 2.7, but this is end-of-life since 2020.  It should only be used as a temporary stepping stone before you migrate your Plone site to Python 3.


## Versions of pip, zc.buildout, setuptools

In Plone core we use these versions to install Plone on Python 2:

```
setuptools==42.0.2
zc.buildout==2.13.8
wheel==0.37.1
```

and these on Python 3:

```
setuptools==65.7.0
zc.buildout==3.0.1
wheel==0.38.4
```

In general you are free to use whatever versions work for you, especially newer ones, but these worked for us.

Note that `setuptools` 66 is more strict with what versions it can recognize.  If you run `pip` or `buildout` and it suddenly cannot find a package with a non-standard version, then this may be the cause.  This is why we stayed at version 65 for Plone 5.2.
`setuptools` 70 will cause problems with current `zc.buildout` 3.0.1, so keep your eyes out for a new `zc.buildout` release.


## Installation

For installation instructions, see the [documentation](https://5.docs.plone.org/manage/installing/index.html).

There is still a [Unified Installer](https://launchpad.net/plone/5.2/5.2.15).  One warning there: we could no longer test this on Python 2.7.  It *should* work though.

For previous Plone 5.2 patch releases we always added all used package distributions on the dist.plone.org server, so you could use this as a "find-link" in Buildout or pip.
This was a historical practice, mostly to have a fallback when a distribution of a third party package was removed from the Python Package Index.
This problem hardly ever happens anymore, so the added value of uploading these distributions is questionable.
It turned out to be harder to gather all packages, so I abandoned it.
If you somehow need this, it should work fine to add the directory of the previous release to the find-links:
https://dist.plone.org/release/5.2.14/
Only a few packages have different versions in 5.2.15.


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
