PLIP 13419: Improvements for user ids and login names
=====================================================

PLIP ticket: https://dev.plone.org/ticket/13419

Review by Ross Patterson (me@rpatterson.net, zenwryly@irc.freenode.net)

The PLIP was reviewed on Ubuntu 12.04 using python 2.7.3 and Chromium 27.


Review steps
------------

- Set up the buildout using the PLIP's config::

  $ bin/buildout -c plips/plip13419-userid-loginname.cfg -N

- Ran tests for the PLIP's auto-checkout packages::

  $ bin/test -s collective.emaillogin4

- Ran tests for the PLIP's patched packages::

  $ bin/test -s Products.CMFPlone -s plone.app.controlpanel -s plone.app.upgrade -s plone.app.users -s Products.PlonePAS

- Reviewed collective.emaillogin4 code

- Reviewed various stuff TTW


Notes and observations
----------------------

- tests pass!

- coverage is pretty good but could be better in some places::

  lines   cov%   module   (path)
    137    21%   collective.emaillogin4.patches.pa_controlpanel.security   (/opt/src/buildout.coredev/src/collective.emaillogin4/collective/emaillogin4/patches/pa_controlpanel/security.py)
     50    18%   collective.emaillogin4.patches.pa_users.personalpreferences   (/opt/src/buildout.coredev/src/collective.emaillogin4/collective/emaillogin4/patches/pa_users/personalpreferences.py)
    226    53%   collective.emaillogin4.patches.pa_users.register   (/opt/src/buildout.coredev/src/collective.emaillogin4/collective/emaillogin4/patches/pa_users/register.py)
      5    40%   collective.emaillogin4.patches.pa_users.utils   (/opt/src/buildout.coredev/src/collective.emaillogin4/collective/emaillogin4/patches/pa_users/utils.py)
      7    28%   collective.emaillogin4.patches.plonepas.property   (/opt/src/buildout.coredev/src/collective.emaillogin4/collective/emaillogin4/patches/plonepas/property.py)

- as discissed in the comment in the PLIP config, these patches
  *should* be merged into the packages they patch.  Let's not make
  more work for our beleaguered release manager.  :-)

- what does the user see if switching email as login "fails when there
  are duplicates" as mentioned in the README.txt?

- I couldn't break anything no matter what I tired>  :-)

- the generated user ids look good


Conclusion
----------

I'm +1 for merge.  I think the implementer should do the merging into
the core packages rather than leaving that to the release manager, but
I'd be fine with implementer merging it into master directly after
we've approved the PLIP for merge.

Well done!
