# Release notes for Plone 6.1.0 final

The first alpha release of Plone 6.1 was a year ago, in January.
The first beta release was in October.
The first and only release candidate was last week.
And now the final 6.1.0 release is here!

The big changes compared to 6.0 are:

* Distributions, the new way to package configuration and content for a new Plone Site.  `plone.volto` and `plone.classicui` are the two core distributions.  You are *very much* invited and challenged to create your own distributions, with help of the new foundational packages `plone.distribution` and `plone.exportimport`.
* `plone.app.multilingual` and `plone.app.discussion` have become core add-ons: no longer in the packages that are pulled in by `Products.CMFPlone`.  If you use the `Plone` Python package you still get them, otherwise you should explicitly add them to your system.
* Classic UI has upgraded the TinyMCE rich text editor from 5 to 7.  It also has a new, more user friendly content browser widget for related items.

A big thank you to all in the Plone community who made this happen over the past year and more.  A lot was accomplished during sprints, while working on company projects, and in spare time.  Your effort, skill, and devotion is seen.  Thank you.

Plone 6.0 has had two years of maintenance support and has reached its end now.  We will probably still do one or two releases the next months, but you are encouraged to start using Plone 6.1.  Both 6.0 and 6.1 have security support until the end of 2027, five years after the release of Plone 6.0.0.

The usual details for 6.1.0:

* Released: February 7, 2025
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-61.html), explaining the biggest changes compared to 6.0.
* Canonical place for these [release notes](https://dist.plone.org/release/6.1.0/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.1.0/changelog.txt).

If you want to jump straight in, here are two important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.1.0/constraints.txt](https://dist.plone.org/release/6.1.0/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.1.0/versions.cfg](https://dist.plone.org/release/6.1.0/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.1.0/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.1.0/versions-ecosystem.cfg).
* Use Docker image `plone-backend` 6.1.0.


## Highlights

There are only small changes since 6.1.0rc1:

* `plone.distribution`: frontend: show id of Plone instance.
* `plone.app.content`: Fix error when folder content type restrictions were set to `No value`.
* `plone.staticresources`: Update `mockup=5.2.0`. See https://github.com/plone/mockup/releases/tag/5.2.0
* `Products.CMFPlone`: Fix modal behaviour after form submission in 404 'not found' page.


## Volto frontend

The default frontend for new Plone 6 sites is Volto.
Note that this is a JavaScript frontend that you need to run in a separate process with NodeJS.

Plone 6.1 is meant to be used with Volto 18.
Latest release is [18.8.1](https://www.npmjs.com/package/@plone/volto/v/18.8.1).  See the [changelog](https://github.com/plone/volto/blob/18.8.1/packages/volto/CHANGELOG.md).


## Classic UI

The HTML based and server side rendered UI that was present in Plone 5.2 and earlier major Plone releases is still available and has also been updated and improved upon in Plone 6.0 and 6.1.  Our documentation now refers to this frontend as 'Classic UI'.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, and 3.13.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
packaging==24.2
pip==24.3.1
setuptools==75.6.0
wheel==0.45.1
zc.buildout==4.0
```

In general you are free to use whatever versions work for you, but these worked for us.

Note that `zc.buildout` 4 has `packaging` as a dependency, so we added a pin for it in the requirements.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
