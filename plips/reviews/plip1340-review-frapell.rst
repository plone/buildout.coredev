PLIP 1340: Get rid of portal_quickinstaller
===========================================

PLIP ticket: https://github.com/plone/Products.CMFPlone/issues/1340

Review by Franco Pellegrini (frapell@gmail.com, frapell@irc.freenode.net)

The PLIP was reviewed on Kubuntu 16.04 using python 2.7.10 and Chromium 51.0.2704.79 Ubuntu 16.04 (64-bit).

August 31, 2016


Review steps
------------

- Set up the buildout using the PLIP's config::

  $ ./bin/buildout -c plips/plip1340-get-rid-of-qi.cfg

- Ran tests for the PLIP's auto-checkout packages::

  $ bin/test -s plone.app.upgrade
  $ bin/test -s Products.ATContentTypes
  $ bin/test -s Products.CMFPlone
  $ bin/test -s Products.CMFQuickInstallerTool
  $ bin/test -s plone.app.testing

- Reviewed code

- Manual testing TTW


Notes and observations
----------------------

Automated testing
+++++++++++++++++

- Tests for plone.app.upgrade pass 100%

- Tests for Products.ATContentTypes pass 100%

- Tests for Products.CMFPlone has 5 errors in the testUnicodeSplitter module, and they are unrelated to the changes for this PLIP

- Tests for Products.CMFQuickInstallerTool pass 100%

- Tests for plone.app.testing pass 100%


Manual testing
++++++++++++++

The following notes are regarding the UI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The UI was listing a previously installed package (plone.app.multilingual) under the "Activated add-ons", so picking up previous packages works fine.

- Uninstalling a product (plone.app.multilingual) also worked fine.

- Pulled in Products.PloneFormGen version 1.8.0. The product doesn't include an uninstall profile, so I got a big warning about it. Installing worked fine, and as expected, it does not allow you to uninstall it.

- Created a test product and installed it. Then, created several upgrade steps, UI showed the product under the "Upgrades" section. Clicking the "Upgrade" button did run all upgrades in the correct order and the package was upgraded.



The following notes are for when using the API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- I think this looks great and consistent, with method names that make sense, a lot of deprecation warnings and every expected common task being taken care of.


Code review
+++++++++++

- Being that the installer is a browser view, there is no way to prevent picking it up with getMultiAdapter, however, I think "get_installer" in core packages, for consistency, should always be used

    https://github.com/plone/Products.CMFPlone/blob/e17ec11434a36b46617f11f3e429fc1b501b67e8/Products/CMFPlone/browser/admin.py#L296

Documentation
+++++++++++++

- Documentation found in https://github.com/plone/Products.CMFPlone/blob/get-rid-of-qi/Products/CMFPlone/GET_RID_OF_QI.rst looks terrific, I would add information about upgrade_product


Conclusion
----------

- I think this looks ready to be merged (After addressing my suggestions about 'get_installer' and completing documentation)
