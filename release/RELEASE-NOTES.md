# Release notes for Plone 6.2.2.1

* Released: October 22nd, 2026
* Check the [release schedule](https://plone.org/download/release-schedule).
* Read the [upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-62.html), explaining the biggest changes compared to 6.1.
* Canonical place for these [release notes](https://dist.plone.org/release/6.2.2.1/RELEASE-NOTES.md) and the full [packages changelog](https://dist.plone.org/release/6.2.2.1/changelog.txt).

If you want to jump straight in, here are some important links:

* With pip you can use the constraints file at [https://dist.plone.org/release/6.2.2.1/constraints.txt](https://dist.plone.org/release/6.2.2.1/constraints.txt).  This includes the extra and ecosystem constraints, which are separate in the Buildout configs.
* With Buildout you can use the versions file at [https://dist.plone.org/release/6.2.2.1/versions.cfg](https://dist.plone.org/release/6.2.2.1/versions.cfg), plus optionally [`versions-extra.cfg`](https://dist.plone.org/release/6.2.2.1/versions-extra.cfg) and [`versions-ecosystem.cfg`](https://dist.plone.org/release/6.2.2.1/versions-ecosystem.cfg).
* Use Docker image `plone-backend`.


## Highlights

This is a security-only release.
These are the main changes compared to 6.2.2:

* `plone.app.content`: Fix information disclosure vulnarability.  See [advisory](https://github.com/plone/plone.app.content/security/advisories/GHSA-vhwp-qc29-j4xp)
* `pip`, `certifi`: Upgrade to versions that fix a [certificate security incident](https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576)
  Note: if you use `uv`, you should upgrade that package yourself to 0.13.4.
* `Pillow`: Upgrade to 13.0.0 for lots of security fixes.  See [Pillow release notes](https://pillow.readthedocs.io/en/stable/releasenotes/13.0.0.html)
  Pillow 13 requires Python 3.11 or higher, so we keep the previous pin for Python 3.10.


## Python compatibility

This release supports Python 3.10, 3.11, 3.12, 3.13, and 3.14.

Note: we will soon drop support for Python 3.10, as this is out of security support.


## pip, buildout, setuptools

In Plone core we use these versions to install Plone:

```
horse-with-no-namespace==20260202.0
pip==26.2.2
setuptools==81.0.0
wheel==0.48.0
zc.buildout==5.2.0
```

In general you are free to use whatever versions work for you, but these worked for us.
If you don't use buildout, it should be fine to use `setuptools` 82+.

You can also try `zc.buildout` 6.0.1.
This includes its own copy of the deprecated `pkg_resources` module, so it works with the latest `setuptools` version.
This can be good if you want to include any security-related fixes from `setuptools`.
And it fixes support for PEP 660 develop packages, so `pyproject.toml` only, made with `setuptools` or with newer build systems like `hatchling`, `flit`, `pdm`.
See the [major changes](https://pypi.org/project/zc.buildout/6.0.1/#user-content-major-changes-in-6-x) for details information.


## Installation

For installation instructions, see the [documentation](https://6.docs.plone.org/install/index.html).


## Issues

If you find any issues, please report them in the [main issue tracker](https://github.com/plone/Products.CMFPlone/issues).
