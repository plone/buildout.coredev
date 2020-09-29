# PLIP 1775: Remove portal_quickinstaller in Plone 6.0

PLIP ticket: https://github.com/plone/Products.CMFPlone/issues/1775

Review by: Alessandro Pisa (<alessandro.pisa@gmail.com>)

Date: August 1, 2020

## Environment

The PLIP was reviewed using:

- Python 3.8.2 Ubuntu 20.04 64-bit
- Chrome Version 84.0.4147.105 (64-bit) Kubuntu 20.04 64-bit


## Jenkins jobs

The plip buildout jobs are good:

- <https://jenkins.plone.org/view/PLIPs/job/plip-1775-quickinstaller-3.6/>
- <https://jenkins.plone.org/view/PLIPs/job/plip-1775-quickinstaller-3.7/>
- <https://jenkins.plone.org/view/PLIPs/job/plip-1775-quickinstaller-3.8/>

The builds are quite old, it might be advisable rebasing/merging
master in the various PRs involved before merging.
I apologize for the delay in reviewing this PLIP.


## PLIP buildout

-   Set up the buildout using the PLIP's config:

    python3.8 -m venv .
    ./bin/buildout -c plips/plip-1775-remove-qi.cfg

Works smooth.

## Involved Packages and related PRs

- https://github.com/plone/Products.CMFPlone/tree/maurits/plip-1775-remove-qi looks good (mostly removal of deprecated code).
- https://github.com/plone/plone.app.upgrade/compare/maurits/plip-1775-remove-qi looks good
  (provides an upgrade step to remove the deprecated tool and adds BBB code).
  There is some commented code that might be better to remove, but this is a minor thing.
- https://github.com/plone/plone.app.testing/compare/maurits/plip-1775-remove-qi looks good
  (mostly removal of deprecated code and updates the documentation).
- https://github.com/plone/plone.app.robotframework/compare/maurits/plip-1775-remove-qi
  (removes deprecated code)

The PRs are still missing.

## Manual testing

I created a fresh Plone site and installed and unistalled an add-on.
I then migrated a Plone5.2 Data.fs and migrated it to Plone 6.
Installing and unistalling add-ons works fine.

## Code review

Most of the changes deal with removing code, so not much to review.
Some of the code in plone.app.upgrade was just commented out.
It might be better to just remove it, unless there is a reason for that
(the commented code happens to be in BBB modules).

Test coverage is given.

Grepping for "quickinstaller" in all the packages shows that there are still
packages with obsolete references to the removed tool (e.g. plone.dexterity and plone.restapi).
It might be a good idea to clean-up at some point.

## Versions

Products.CMFPlone and plone.app.upgrade towncrier entries report breaking changes.
plone.app.testing and plone.app.robotframework towncrier entries report new features.

This seems correct.

## Documentation

Most of the documentation about the new installer was already provided in the PLIP
https://github.com/plone/Products.CMFPlone/issues/1340.
The remaining corrections related to the fact the tool is removed are correctly
added in the reviewd branches.

## Conclusion

The PLIP is ready to be merged.
