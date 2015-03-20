.. -*- coding: utf-8 -*-

=====================
Plone Release Process
=====================

1. Check Jenkins Status

Check latest Plone coredev job on jenkins.plone.org,
it should be green,
if it is not,
fix the problem first.

2. Check out buildout.coredev

git clone git@github.com:plone/buildout.coredev.git
git checkout 5.0
python bootstrap.py
bin/buildout -c release.cfg

3. Check Packages for Updates

Check all packages for updates,
add to/remove from checkouts.cfg accordingly.

TODO: Add esteele.manager command for checks.

This step might become obsolete in the future if we do the check for every single commit.

4. Check packages individually

  a) Check changelog
     (Check if CHANGES.rst is up-to-date,
     all changes since the last release should be included?
     Compare "git log HEAD...<LAST_RELESE_TAG>" with CHANGES.rst)

  b) Run `checkmanifest <https://pypi.python.org/pypi/check-manifest/>`_ (TODO: Include in zest.releaser/esteele.manager)

  c) Check package "best practices" (README.rst, CHANGES.rst, src directory)

    - Check if version in setup.py is correct and follows our versioning best practice

  d) Make a release (zest.releaser: "bin/fullrelease")

  e) Remove packages from auto-checkout section and update versions.cfg (automated by esteele.manager)

5. Make sure plone.app.upgrade contains an upgrade step for the future Plone release.

6. Update CMFPlone version in ``profiles/default/metadata.xml``

7. Write an email to the translation team,
   asking them to do a plone.app.locales release.

8. Ask Rok to make a plone.app.widgets release (TODO!)

9. Create a pending release (directory) on dist.plone.org

10. Write an email to the Plone developers list announcing a pending release.

11. Inform the QA team about a new pending release.

12. Update plone.app.locales version.

13. Make final release on dist.plone.org (remove "-pending")

14. Update the "-latest" link on dist.plone.org

15. Create a unified changelog (TODO: needs to be documented, esteele.manager)

16. Create new release on launchpad (https://launchpad.net/plone/)

17. Create release page on http://plone.org/products/plone/releases

18. Send links to installers list
    (plone-installers@lists.sourceforge.net <mailto:plone-installers@lists.sourceforge.net>)

19. Wait for installers to be uploaded to Launchpad,
    link on plone.org release page

20. Mark release page as "final" (launchpad?)

20. Update PloneSoftwareCenter pointer to the newest release,
    so that it's linked from the homepage

21. Send out announcement to plone-announce

22. Update #plone topic


`esteele.manager <https://github.com/esteele/esteele.manager/>`_ has a script to handle:

- Checking all packages for updates, modify versions.cfg/checkouts.cfg accordingly (#1 above)
- zest.releaser hooks to:

  - Check to make sure the user has permission to upload the release to
    pypi
  - Update versions.cfg/checkouts.cfg after the package is released. (#)
