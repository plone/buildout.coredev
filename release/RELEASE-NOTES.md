# Release notes for Plone 5.2.13

* Released: Thursday July 20, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://5.docs.plone.org/manage/upgrading/version_specific_migration/upgrade_to_52.html), explaining the biggest changes compared to 5.1.
* Canonical place for these [release notes](https://dist.plone.org/release/5.2.13/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/5.2.13/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/5.2.13/constraints.txt](https://dist.plone.org/release/5.2.13/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/5.2.13/versions.cfg](https://dist.plone.org/release/5.2.13/versions.cfg).


## Highlights

Major changes since 5.2.12:

* `plone.app.locales`: Update Italian translations.
* `Products.CMFPlone`: Drop Python 3.7 support.


## Python compatibility

This release supports Python 2.7 and 3.8.

**Important: This release no longer officially supports Python 3.7.**
Python 3.7 has reached end-of-life in June.
We have stopped testing on 3.7 and no longer provide specific version pins for 3.7 (none seem needed at the moment though).  This means that things may start breaking without being noticed.  If something breaks and you can supply a fix, we are happy to include it in the next release though.

Plone 5.2 still supports Python 2.7, but this is end-of-life since 2020.  It should only be used as a temporary stepping stone before you migrate your Plone site to Python 3.

The next release is scheduled for October 2023, and is planned to be the last regular release of Plone 5.2.
After that release, there is still one year of security support.


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

Note that `setuptools` 66 is more strict with what versions it can recognize.  If you run `pip` or `buildout` and it suddenly cannot find a package with a non-standard version, then this may be the cause.  This is why we stayed at version 65 for this release.  Likely, we will keep doing this for future Plone 5.2 releases.


## Installation

For installation instructions, see the [documentation](https://5.docs.plone.org/manage/installing/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
