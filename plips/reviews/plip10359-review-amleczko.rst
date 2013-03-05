PLIP 10359: Convert control panels to use z3c.form
==================================================

PLIP ticket: https://dev.plone.org/ticket/10359

Review by Andrew Mleczko (amleczko@redturtle.it, amleczko on IRC)

The PLIP was reviewed on Ubuntu 12.04 using python 2.7.3 and Chromium 23,
Firefox 18.0


Review steps
------------

- Ran buildout using the plip10359-z3cform-controlpanel.cfg file.

TODO

- Ran tests for the PLIP's auto-checkout packages::

  $ bin/test -s plone.app.controlpanel -s plone.app.discussion -s plone.app.registry
  $ bin/test -s Products.CMFPlone

- Reviewed the code changes the PLIP's auto-checkout packages

Notes and observations
----------------------

Tests wouldn't run under newest versions in coredev 4.3::

        Failure in test plone.coredev/src/plone.app.controlpanel/plone/app/controlpanel/tests/filter.txt
        Traceback (most recent call last):
        File "/usr/lib/python2.7/unittest/case.py", line 327, in run
            testMethod()
        File "/usr/lib/python2.7/doctest.py", line 2201, in runTest
            raise self.failureException(self.format_failure(new.getvalue()))
        AssertionError: Failed doctest test for filter.txt
        File "plone.coredev/src/plone.app.controlpanel/plone/app/controlpanel/tests/filter.txt", line 0

        ----------------------------------------------------------------------
        File "plone.coredev/src/plone.app.controlpanel/plone/app/controlpanel/tests/filter.txt", line 66, in filter.txt
        Failed example:
            print_all_of('nasty_tags')
        Expected:
            applet
            embed
            meta
            object
            script
            style
        Got nothing


            11/68 (16.2%)

        Failure in test plone.coredev/src/plone.app.controlpanel/plone/app/controlpanel/tests/search.txt
        Traceback (most recent call last):
        File "/usr/lib/python2.7/unittest/case.py", line 327, in run
            testMethod()
        File "/usr/lib/python2.7/doctest.py", line 2201, in runTest
            raise self.failureException(self.format_failure(new.getvalue()))
        AssertionError: Failed doctest test for search.txt
        File "plone.coredev/src/plone.app.controlpanel/plone/app/controlpanel/tests/search.txt", line 0

        ----------------------------------------------------------------------
        File "plone.coredev/src/plone.app.controlpanel/plone/app/controlpanel/tests/search.txt", line 89, in search.txt
        Failed example:
            'Event' in site_props.types_not_searched
        Expected:
            False
        Got:
            True


Conclusion
----------
