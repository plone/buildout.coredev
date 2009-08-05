This is the development buildout for Plone 4.0.

Plone 4 now runs Zope 2.12, and uses Python 2.6, so make sure that
you're using the correct version of Python to run the 'python bootstrap.py'
command.

================
= mr.developer =
================

 This buildout uses mr.developer to manage package development. See
http://pypi.python.org/pypi/mr.developer for more information or run
'bin/develop help' for a list of available commands.

=======================
= PLIP Implementation =
=======================

 Create a buildout configuration file for your plip in the 'plips' folder.
Give it a descriptive name, starting with the plip number;
'plip-1234-widget-frobbing.cfg' for example. This file will define the
branches/trunks you're working with in your PLIP. It should look something
like this:

 In file plips/plip-1234-widget-frobbing.cfg...

 [buildout] 
 extends = plipbase.cfg
 auto-checkout +=
  plone.somepackage
  plone.app.someotherpackage

 [sources] 
  plone.somepackage = svn https://svn.plone.org/.../branches/plip-1234-widget-frobbing
  plone.app.someotherpackage = svn https://svn.plone.org/.../branches/plip-1234-widget-frobbing

 [instance] 
 eggs += 
    plone.somepackage
    plone.app.someotherpackage
 zcml +=
    plone.somepackage
    plone.app.someotherpackage

Use the same naming convention when branching existing packages, and you
should always be branching packages when working on PLIPs.

=================
= Common Issues =
=================
 
Issue:
-----

"ERROR: Can't update package '[Some package]', because it's dirty."

Fix:
---

 mr.developer is complaining because a file has been changed/added, but not
 committed.

 Use "bin/develop update --force". Adding "*.pyc *~.nib *.egg-info
 .installed.cfg *.pt.py *.cpt.py *.zpt.py *.html.py *.egg" to your subversion
 config's global-ignores has been suggested as a more permanent solution.

Issue:
-----

"ImportError: No module named Zope2" when building using a PLIP cfg file.

Fix:
---
 
 Appears to not actually be the case. Delete 'mkzopeinstance.py' from bin/ and
 rerun buildout to correct this if you're finding it irksome.

Issue:
-----

can't open file '/Startup/run.py'

Fix:
---

Two possible fixes, you are using Python 2.4 by mistake, so use Python 2.5 or 2.6 instead.
Or, you may need to make sure you run 'bin/buildout …' after 'bin/develop …'.
Try removing parts/*, bin/*, .installed.cfg, then re-bootstrap and re-run
buildout, develop, buildout.

Issue:
-----

Missing PIL.

Fix:
---
 
PIL.cfg is include within this buildout to aid in PIL installation. 
Run bin/buildout -c PIL.cfg to install. This method does not work on Windows, so
we're unable to run it by default.