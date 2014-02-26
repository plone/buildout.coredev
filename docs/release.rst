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
9. Announce the soft-release to plone-dev, plone-qa
10. (...wait...)
11. Move from -pending to final.
12. Update -latest links
13. Create new release on launchpad (https://launchpad.net/plone/)
14. Create release page on http://plone.org/products/plone/releases
15. Send link to installers list (plone-installers@lists.sourceforge.net
<mailto:plone-installers@lists.sourceforge.net>)
16. Wait for installers to be uploaded to Launchpad, link on plone.org
release page
17. Mark release page as "final"
18. Update PloneSoftwareCenter pointer to the newest release, so that
it's linked from the homepage
19. Send out announcement to plone-announce

https://github.com/esteele/esteele.manager/ has a script to handle
#1 and zest.releaser hooks that take care of updating versions.cfg/checkouts.cfg after a package is released.


#1 Check all packages for updates
---------------------------------

- Check if CHANGES.rst is up-to-date (are all changes since the last release
  included?)
- Check if version in setup.py is correct (alpha, beta, final release version)
- Check if MANIFEST.in includes all files (README.rst, CHANGES.rst)
- Check if pkg follows best practice (README.rst, CHANGES.rst, src directory)
- Make release ("bin/fullrelease")
- Remove pkg from checkouts.cfg auto-checkout section
- Add release to versions.cfg
- Run local buildout (to make sure the package is installable)
- Run pkg tests (run alltests)

MANIFEST.in::

  include *.txt
  include *.rst

  recursive-include docs *
  recursive-include plone *

  global-include *.mo
  global-exclude *.pyc
