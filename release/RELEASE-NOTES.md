# Release notes for Plone 6.0.0rc1 (unreleased)

Updated: Thursday November 17, 2022.

## Highlights

Major changes since 6.0.0b3:

* Various packages: updates to support Python 3.11.  See below.

* Zope 5.7: This feature release adds full support for Python 3.11 and a ZPublisher encoder for inputting JSON data.
  See the [Zope changelog](https://github.com/zopefoundation/Zope/blob/5.7/CHANGES.rst) for details.

* `zc.buildout`: After long development this has a final release.  We use version 3.0.1, which now works nicely with latest pip (using 22.3.1).
  Note that it is usually fine if you use different versions of `zc.buildout`, `pip`, `setuptools`, and `wheel`.  We just pin versions that we know work at the moment.

* `plone.restapi`:

  * Added `@upgrade` endpoint to preview or run an upgrade of a Plone instance.

  * Added `@rules` endpoint with GET/POST/DELETE/PATCH.

  * Added link integrity support for slate blocks.

* `plone.scale`: Add support for animated GIFs.


## Volto frontend

The default frontend for Plone 6 is Volto. Latest release is [16.0.0-alpha.50](https://www.npmjs.com/package/@plone/volto/v/16.0.0-alpha.50).
See the [changelog](https://github.com/plone/volto/blob/16.0.0-alpha.50/CHANGELOG.md).


## Python compatibility

This release supports Python 3.8, 3.9, 3.10, and 3.11.

Python 3.11.0 was released in October and we are proud to already be able to say Plone supports it!  All tests pass.
This is expected to be faster than other Python versions.
Note that not all add-ons may work yet on 3.11, but in most cases the needed changes should be small.

A big thank you for this goes to the Zope part of the Plone community, especially Jens Vagelpohl and Michael Howitz.
The trickiest parts of the fixes for 3.11 were needed on the Zope level, for example `RestrictedPython` and packages with C code.

A word of warning: Plone on 3.11 should work fine on Linux, but you may have *trouble installing it on Windows and Mac*.
Forgive me for using some technical terms here.
The problem is Python packages that have C code.  Not all these packages may have "wheels" (a Python distribution file) available for your operating system and architecture.

* On Windows you may not be able to install the `lxml` dependency.  A new 4.9.2 release should fix this.

* On Mac, a package may have a wheel for the Intel architecture and not for ARM, or the other way around, or your Mac may need an unavailable "universal2" wheel.

In all cases, if you have the right compilers and other development tools available, then you should be able to get it working on Windows and Mac, but this can be tricky.  If you don't want to spend hours, you may want to wait a bit.


## Installation

For installation instructions, see the [documentation](https://6.dev-docs.plone.org/install/index.html).
This documentation is under development, but this should get you up and running.  No worries.
