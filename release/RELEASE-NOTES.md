# Release notes for Plone 5.2.14

* Released: Thursday September 21, 2023
* This is expected to be the last maintenance release.
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://5.docs.plone.org/manage/upgrading/version_specific_migration/upgrade_to_52.html), explaining the biggest changes compared to 5.1.
* Canonical place for these [release notes](https://dist.plone.org/release/5.2.14/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/5.2.14/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/5.2.14/constraints.txt](https://dist.plone.org/release/5.2.14/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/5.2.14/versions.cfg](https://dist.plone.org/release/5.2.14/versions.cfg).


## Highlights

Major changes since 5.2.13:

* This includes security fixes from today's announcement:
  * https://community.plone.org/t/plone-security-advisory-2023-09-21/17941
  * https://plone.org/security/hotfix/20230921
* `Zope`:
  * Security fixes in `AccessControl` and `RestrictedPython`.  See [community announcement](https://community.plone.org/t/zope-4-8-9-and-5-8-4-released-with-a-security-fix/17849).
  * Allow only some image types to be displayed inline. Force download for others, especially SVG images.
  * Tighten down the ZMI frame source logic to only allow site-local sources.
* `plone.namedfile`: Fix stored XSS (Cross Site Scripting) for SVG images.
* `plone.rest`: When ``++api++`` is in the url multiple times, redirect to the proper url.
* `plone.restapi`:
  * Fix stored XSS (Cross Site Scripting) for SVG image in user portrait.
* `Products.CMFCore`: Make `decodeFolderFilter` and `encodeFolderFilter` non-public.
  This is the workaround from [CVE-2023-36814](https://github.com/zopefoundation/Products.CMFCore/security/advisories/GHSA-4hpj-8rhv-9x87).
* `plone.app.multilingual`:
  * Fix various problems when using the Indonesian language in a multilingual setup.
    This language has ``id`` as code.  This is not allowed as an id in Plone, so it has always been created as ``id-id`` instead.
    This needs some special handling.
  * Fix ``set_recursive_language`` to actually find child objects.  This is used to make sure that a language folder only contains content in this language.


## Last maintenance release

Plone 5.2.14 is planned to be the last regular release of Plone 5.2.
This release was originally planned for October, but we moved it forward to have the security fixes in a full release.  If there are good reasons, we can still make a new release.

After October 2023, Plone 5.2 is out of maintenance support.

There is still one year of security support, until October 31, 2024.
At that moment, even Python 3.8 is out of security support by the Python community.


## Python compatibility

This release supports Python 2.7 and 3.8.

Python 3.6 and 3.7 should still work, but these are end of life and no longer supported.

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


## Installation

For installation instructions, see the [documentation](https://5.docs.plone.org/manage/installing/index.html).

There is still a [Unified Installer](https://launchpad.net/plone/5.2/5.2.14).  One warning there: we could no longer test this on Python 2.7.  It *should* work though.

## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
