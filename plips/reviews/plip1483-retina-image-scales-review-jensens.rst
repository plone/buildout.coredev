PLIP 1483: Retina Image Scales
==============================

PLIP ticket
    https://github.com/plone/Products.CMFPlone/issues/1483

Review by
    Jens Klein (jens@bluedynamics.com)

Environment
    The PLIP was reviewed on Ubuntu 14.04 using python 2.7.12 and Firefox 51 (64-bit).

Date
    March 4, 2017

Involved Packages and its pull requests
---------------------------------------

Plone Core

- https://github.com/plone/Products.CMFPlone/issues/1611
- https://github.com/plone/plone.namedfile/issues/25
- https://github.com/plone/plone.app.upgrade/issues/76
- https://github.com/plone/plone.app.portlets/issues/72
- https://github.com/plone/plone.app.contenttypes/issues/350
- https://github.com/plone/documentation/issues/781

Plus some others fixing issues, but they are all already merged.


Review steps
------------

- Check state of jenkins job on http://jenkins.plone.org/view/PLIPs/job/plip-1483-retina-image-scales/

- Set up the buildout using the PLIP's config::

  $ ./bin/buildout -c plips/plip-1483-retina-image-scales.cfg

- Ran single tests for the PLIP's auto-checkout packages::

  $ test -s Products.CMFPlone
  $ test -s plone.namedfile
  $ test -s plone.app.upgrade
  $ test -s plone.app.portlets
  $ test -s plone.app.contenttypes
  $ test -s documentation

- Review code

- Manual testing TTW


Notes and observations
----------------------

Automated testing
+++++++++++++++++

- tests of jenkins job are ?green/red.
- tests of ``Products.CMFPlone`` are
- tests of ``plone.namedfile`` are
- tests of ``plone.app.upgrade`` are
- tests of ``plone.app.portlets`` are
- tests of ``plone.app.contenttypes`` are
- tests of ``documentation`` are

- combined PLIP test job ?? on jenkins.

Manual testing
++++++++++++++

todo

Code review
+++++++++++


Versions
++++++++

Check if semantic versioning applies.

- ``Products.CMFPlone``
- ``plone.namedfile``
- ``plone.app.upgrade``
- ``plone.app.portlets``
- ``plone.app.contenttypes``
- ``documentation``


Documentation
+++++++++++++

Documentation was written and looks good!


Conclusion
----------

I propose to merge/not merges this PLIP.
