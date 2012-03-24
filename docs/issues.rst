Common Issues
=============

Issue
-----

"ERROR: Can't update package '[Some package]', because it's dirty."

Fix
^^^

mr.developer is complaining because a file has been changed/added, but not
committed.

Use ``bin/develop update --force``. Adding ``*.pyc *~.nib *.egg-info
.installed.cfg *.pt.py *.cpt.py *.zpt.py *.html.py *.egg`` to your subversion
config's global-ignores has been suggested as a more permanent solution.

Issue
-----

``ERROR: You are not in a path which has mr.developer installed (.mr.developer.cfg not found).``

When running any ``./bin/develop`` command.

Fix
^^^

``ln -s plips/.mr.developer.cfg``

Issue
------

"ImportError: No module named Zope2" when building using a PLIP cfg file.

Fix
^^^

Appears to not actually be the case. Delete 'mkzopeinstance.py' from bin/ and
rerun buildout to correct this if you're finding it irksome.

Issue
-----

can't open file '/Startup/run.py'

Fix
^^^

Two possible fixes, you are using Python 2.4 by mistake, so use Python 2.5 or
2.6 instead. Or, you may need to make sure you run 'bin/buildout …' after
'bin/develop …'. Try removing parts/*, bin/*, .installed.cfg, then re-bootstrap
and re-run buildout, develop, buildout.

Issue
-----

Missing PIL.

Fix
^^^

pil.cfg is include within this buildout to aid in PIL installation. Run
bin/buildout -c pil.cfg to install. This method does not work on Windows, so
we're unable to run it by default.


Issue
-----

bin/develop status is showing that the Products.CMFActionIcons egg has been
modified, but I haven't touched it.  And this is preventing bin/develop up
from updating all the eggs.

Fix
^^^

Edit ~/.subversion/config and add eggtest*.egg to the list of global-ignores

