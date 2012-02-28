PLIP 11838: Add z3c support to plone.app.portlets
========================================
Ticket: https://dev.plone.org/ticket/11838

Review by Alec Mitchell (alecpm@gmail.com, alecm on irc) The PLIP was
reviewed on Mac OS X 10.6.8 using python 2.7.2 and Google Chrome
17.0.963.56

Review Steps
------------

 - Reviewed code changes at
 https://svn.plone.org/svn/plone/plone.app.portlets/branches/plip11838-z3c-portlets

 - Ran package tests and code coverage

 - Created small package with simple z3c.form based portlet and tested
 it in local instance.


Notes and Oberservations
------------------------

 - Developer documentation is a must for this kind of PLIP.  This PLIP
 essentially provides yet another way to do something that's already
 reasonably documented.  This needs to be at least as well documented,
 especially if we want to promote it as the "correct" way forward.

 - Tests appear to be well written and all package tests pass.  Test
 coverage on browser/z3cformhelper.py is only 38%, and there appears
 to be essentially no coverage of any python logic.
 Testing that code will probably require browser tests (since the
 logic is nearly all wrapped in form button handlers).  It would be
 nice to see this improved, but the code is essentially all
 boilerplate z3c.form code, so I don't consider it critical.

 - It seems a little strange that there's a canonical/convenience
 import location for formlib portlet base forms in
 ``plone.app.portlets.portlets.base`` whereas the z3c.form base form
 classes need to be imported from
 ``plone.app.portlets.browser.z3cformhelper``.  Perhaps there could be
 a more consistent import alias for the new form classes.
 
 - Other than the potential for developer confusion about the right
 way to make portlets going forward, there don't appear to be any
 significant risks involved in the PLIP and its implementation.

Conclusion
----------

Developer documentation is needed, additionally it may make sense to
consider a ZopeSkel recipe to provide a base for z3c.form based
portlets.  Some browser tests that ensure the basic form actions
behave as they should would be helpful also.  It is essentially ready,
but without updated documentation I am +0.
