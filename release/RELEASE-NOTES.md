# Release notes for Plone 5.2.11rc1

* Released: Thursday January 26, 2023
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://5.docs.plone.org/manage/upgrading/version_specific_migration/upgrade_to_52.html), explaining the biggest changes compared to 5.1.
* Canonical place for these [release notes](https://dist.plone.org/release/5.2-dev/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/5.2-dev/changelog.txt).

For technical wizards who want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/5.2-dev/constraints.txt](https://dist.plone.org/release/5.2-dev/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/5.2-dev/versions.cfg](https://dist.plone.org/release/5.2-dev/versions.cfg).


## Highlights

Major changes since 5.2.10:

* `Zope`:
  * Set the published default Content-Type header to text/plain if none has been set explicitly to prevent a cross-site scripting attack.  Also remove the old behavior of constructing an HTML page for published methods returning a two-item tuple.  This fix was already included in Plone 5.2.10.1 and 5.2.10.2.
  * Various other packages have fixes for this to avoid regressions.
* `plone.app.caching`: Apply weak caching to GET requests of content with application/json, handled by `plone.restapi`. See [`plone.rest` issue 73](https://github.com/plone/plone.rest/issues/73).
* `Products.CMFPlone`: When autologin after password reset is enabled (this is the default), use the same adapters as during normal login. Specifically: the `IInitialLogin` and `IRedirectAfterLogin` adapters.


## Python compatibility

This release supports Python 2.7, 3.7, and 3.8.

Python 3.6 support was [dropped in Plone 5.2.10](https://community.plone.org/t/plone-5-2-drops-python-3-6-support/15706).
Note that both Python 2.7 and 3.6 have reached end of life, and Python 3.7 will reach end of life in June 2023.
Plone 5.2 supports Python 2.7, but it should only be used as a temporary stepping stone before you migrate your Plone site to Python 3.


## Versions of pip, zc.buildout, setuptools

Plone 5.2 ships with a `requirements.txt` that pins `pip`, `zc.buildout`, `setuptools`, and `wheel` (plus a few more unpinned packages when you are on Windows).  In the `versions.cfg` for Buildout we have the same versions.
We have been very conservative with these versions.  The main reason is that we wanted to use the same versions for Python 2 and 3.

This is starting to harm the Python 3 side.  See one personal ["war" story](https://github.com/zopefoundation/zope.container/issues/48) on Mac where one package could be installed on Python 3.8.13, but not on 3.8.14 or higher.  Using the latest versions of pip and Buildout and friends, all was well.
So starting with Plone 5.2.11, we pin different versions of these packages on Python 2 and 3.

You should know that you are free to use whatever versions you like for these tools.  Use whatever versions work on your system, especially on Python 3.
Note that in a `buildout.cfg` you can "unpin" versions to tell Buildout to just use whatever has already been installed by pip:

```
[buildout]
newest = false

[versions]
pip =
setuptools =
wheel =
zc.buildout =
```


## Installation

For installation instructions, see the [documentation](https://5.docs.plone.org/manage/installing/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
