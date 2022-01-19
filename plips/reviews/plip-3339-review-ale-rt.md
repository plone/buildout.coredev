# PLIP 3339: Replace z3c.autoinclude with plone.autoinclude

PLIP ticket: <https://github.com/plone/Products.CMFPlone/pull/3340>

Review by: Alessandro Pisa (<alessandro.pisa@gmail.com>)

Date: November 28, 2021

## Environment

The PLIP was reviewed using Python 3.8.10 and Ubuntu 20.04 64-bit.

## Jenkins jobs

The plip buildout jobs are green:

- <https://jenkins.plone.org/view/PLIPs/job/plip-3339-plone-autoinclude-3.7/>
- <https://jenkins.plone.org/view/PLIPs/job/plip-3339-plone-autoinclude-3.8/>
- <https://jenkins.plone.org/view/PLIPs/job/plip-3339-plone-autoinclude-3.9/>

## PLIP buildout

I ran buildout using the PLIP's config:

```
cd plips && ../bin/buildout -c plip-3339-plone-autoinclude.cfg && cd ..
```

It works smoothly.

The PLIP buildout is really simple. It introduces the new `plone.autoinclude` package and specifies a branch for CMFPlone.

I made a PR to `buildout.coredev` to add (<https://github.com/plone/buildout.coredev/pull/755>):

```
[sources]
plone.autoinclude = git ${remotes:plone}/plone.autoinclude.git pushurl=${remotes:plone_push}/plone.autoinclude.git branch=main

[versions]
plone.autoinclude = 1.0.0a2
```

Then the PR <https://github.com/plone/Products.CMFPlone/pull/3340> can be tested as a regular PR.

## Testing

I started an existing instance with the PLIP buildout and all went fine.

I noticed that the `plone.autoinclude` package is quite verbose (see <https://github.com/plone/plone.autoinclude/issues/11>).

I tested some add-ons:

- plone.gallery
- plone.app.debugtoolbar

They work smoothly.

I also tested the `plone.autoinclude` package on Plone 5.2 adding to a pretty comlex installation the following lines:
```
eggs +=
    plone.autoinclude
zcml +=
    plone.autoinclude.ploneinclude-meta
    plone.autoinclude.ploneinclude
    plone.autoinclude.ploneinclude-overrides
```
and changing the entry point in my package from `[z3c.autoinclude.plugin]` to `[plone.autoinclude.plugin]`.

I did not spot any issue.

## Code review

The code passes tests with:

- isort
- black
- flake8
- pyroma
- check-manifested

Most of them of those QA checks are present in the `tox.ini` of the package and there is a GHA that runs on every pull request.

Scanning the code I did not spotted anything except that it appears to be well written and thought.

## Documentation

The documentation in the repository README is excellent. See <https://github.com/plone/plone.autoinclude/blob/main/README.rst>.

There are a couple of topics that would be nice to have covered in the section `For add-on authors`:

- guide the add-ons writer to replace `includeDependencies`
- some lines about when to use the `module` option (I think it is needed when `plone.autoinclude` logs the exception `Could not import {module_name}`)

This we help the people that are skimming the documentation, given that they are already covered in other sections.

In the core packages there are still some references to `includeDependencies`, see e.g. <https://github.com/plone/plone.app.dexterity/search?q=includeDependencies>

All these refinements can be done also after the PLIP is merged.

## Risks

If I am not mistaken we have only two changes required, for the add-ons authors, in order to make the existing add-ons compatible with this PLIP:
1. replace `includeDependencies`
2. specify the `module` name when it is different from the package name

Risk 1. was mentioned in the PLIP text and the usage of `includeDependencies` is discourgaed since quite some time.
Risk 2. was not mentioned.

I am willing to take risk 2. as well:
- the chance of having to deal with such packages is pretty limited
- Plone 6 will be a major release, this kind of changes is acceptable

## Conclusion

The PLIP implementation is complete.
The job was done with an impressive quality.
The additional risk can cause some troubles to a limited number of Plone users and Plone 6 will be anyway a major release.

Given that, I am definitely in favour of merging the related PRs:

- <https://github.com/plone/buildout.coredev/pull/755>
- <https://github.com/plone/Products.CMFPlone/pull/3340>
