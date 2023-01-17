# Release notes for Plone 5.2.10.2

* Released: Wednesday December 21, 2022
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://5.docs.plone.org/manage/upgrading/version_specific_migration/upgrade_to_52.html), explaining the biggest changes compared to 5.1.
* Canonical place for these [release notes](https://dist.plone.org/release/5.2.10.2/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/5.2.10.2/changelog.txt).

For technical wizards who want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/5.2.10.2/constraints.txt](https://dist.plone.org/release/5.2.10.2/constraints.txt)
* With Buildout you can use the versions file at [https://dist.plone.org/release/5.2.10.2/versions.cfg](https://dist.plone.org/release/5.2.10.2/versions.cfg).


## Highlights

Major changes since 5.2.10.1:

* `plone.app.blocks`: Fix regression after Zope security fix. The `layout_view` was rendered as plain text instead of html.
  Note that this is not used by core Plone, but is in use by several tile-related ecosystem packages, for example Mosaic.

* Zope: revert updates to dependency package versions.

  * Plone 5.2.10 extends the versions.cfg or constraints from Zope 4.8.3.
  * Plone 5.2.10.1 extends the versions.cfg or constraints from Zope 4.8.6. This has the security fix and related regression fixes, plus lots of dependency package updates.  This includes a Datetime update which can cause problems on Python 2.  There may be other problems that we have not seen yet.
  * Plone 5.2.10.2 now extends the versions.cfg or constraints from Zope 4.8.3, and only overrides the Zope version pin to 4.8.6.  So you have the security fix and related regression fixes, but keep the dependency package versions the same as originally.


## Python compatibility

This release supports Python 2.7, 3.7, and 3.8.

Python 3.6 support was [dropped in Plone 5.2.10](https://community.plone.org/t/plone-5-2-drops-python-3-6-support/15706).
Note that both Python 2.7 and 3.6 have reached end of life, and Python 3.7 will reach end of life in June 2023.
Plone 5.2 supports Python 2.7, but it should only be used as a temporary stepping stone before you migrate your Plone site to Python 3.


## Versions of pip, zc.buildout, setuptools

Plone 5.2 ships with a `requirements.txt` that pins `pip`, `zc.buildout`, `setuptools`, and `wheel` (plus a few more unpinned packaged when you are on Windows).  In the `versions.cfg` for Buildout we have the same versions.
We have been very conservative with these versions.  The main reason is that we wanted to use the same versions for Python 2 and 3.

This is starting to harm the Python 3 side.  See one personal ["war" story](https://github.com/zopefoundation/zope.container/issues/48) on Mac where one package could be installed on Python 3.8.13, but not on 3.8.14 or higher.  Using the latest versions of pip and Buildout and friends, all was well.
So the next Plone 5.2 version may very well pin different versions of these packages on Python 2 and 3.

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
