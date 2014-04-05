=====================
Plone Release Process
=====================

1. Check all packages for updates, add to/remove from checkouts.cfg accordingly
2. Wait for green light from Jenkins
3. Tag, release all packages
4. Update versions.cfg, checkouts.cfg accordingly
5. Make release (pending) directory on dist.plone.org
6. Upload sdist packages
7. Add versions.cfg
8. Generate unified changelog
9. Notify i18n-team of upcoming release
10. Announce the soft-release to plone-dev, plone-qa
11. (...wait...)
12. Update plone.app.locales version
13. Move from -pending to final.
14. Update -latest links
15. Create new release on launchpad (https://launchpad.net/plone/)
16. Create release page on http://plone.org/products/plone/releases
17. Send links to installers list (plone-installers@lists.sourceforge.net
<mailto:plone-installers@lists.sourceforge.net>)_
18. Wait for installers to be uploaded to Launchpad, link on plone.org
release page
19. Mark release page as "final"
20. Update PloneSoftwareCenter pointer to the newest release, so that
it's linked from the homepage
21. Send out announcement to plone-announce
22. Update #plone topic


`esteele.manager<https://github.com/esteele/esteele.manager/>`_ has a script to handle:
- Checking all packages for updates, modify versions.cfg/checkouts.cfg
  accordingly (#1 above)
- zest.releaser hooks to:
  - Check to make sure the user has permission to upload the release to
    pypi
  - Update versions.cfg/checkouts.cfg after the package is released. (#)


#1 Check all packages for updates
---------------------------------

- Check if CHANGES.rst is up-to-date (are all changes since the last release
  included?) => (compare "git log HEAD...<LAST_RELESE_TAG>" with CHANGES.rst)

- Check if version in setup.py is correct and follows our versioning best practice (where to find this best practice?)

- Check if MANIFEST.in includes all files (README.rst, CHANGES.rst)

- Check if pkg follows best practice (README.rst, CHANGES.rst, src directory)

- Commit and push changes if necessary.

- Make release ("bin/fullrelease")

- Delete pkg from src directory (e.g. "rm -rf plone.app.layout")

- Remove pkg from checkouts.cfg auto-checkout section

- Update package version in versions.cfg

- Run local buildout (to make sure the package is installable)

- Run pkg tests (e.g. "bin/test -s plone.app.layout")

- Push Changes (Since we always start on a green build, we do not have to wait for Jenkins finish the build (the releas)

MANIFEST.in::

  include *.txt
  include *.rst

  recursive-include docs *
  recursive-include plone *

  global-include *.mo
  global-exclude *.pyc
