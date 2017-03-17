PLIP 1483: Retina Image Scales
==============================

PLIP ticket
    https://github.com/plone/Products.CMFPlone/issues/1483

Review by
    Jens Klein (jens@bluedynamics.com)

Environment
    The PLIP was reviewed on Ubuntu 14.04 using python 2.7.12 and Firefox 51 (64-bit).

Date
    March 17, 2017

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

- Ran single tests local for the PLIP's auto-checkout packages::

  $ bin/test -s Products.CMFPlone
  $ bin/test -s plone.namedfile
  $ bin/test -s plone.app.upgrade
  $ bin/test -s plone.app.portlets
  $ bin/test -s plone.app.contenttypes

- Review code

- Manual testing TTW


Notes and observations
----------------------

Automated testing
+++++++++++++++++

- tests of jenkins PLIP test job are green
- tests of ``Products.CMFPlone`` are passing.
- tests of ``plone.namedfile`` are passing.
- tests of ``plone.app.upgrade`` are passing.
- tests of ``plone.app.portlets`` are passing.
- tests of ``plone.app.contenttypes`` are passing.

Manual testing
++++++++++++++

I created a fresh Plone instance and set the "Retina mode" to "Enabled (2x, 3x)".

I uploaded two images (PNG and JPG).

On an old-style screen (1600x900) it seems the quality decreased.
This is probably primary b/c of the low default imagesquality settings.

On an Android Mobile Phone (Oneplus Two) images are very crisp and the result is a huge enhancement.


Code review
+++++++++++

Code style and readability is overall good for. Page templates improved slighlty.

Test coverage is given.

Overall I refer to Johannes Raggam's review notes and agree with him.

OTOH I do not see this as a blocker for merging the PLIP, but do recommend to improve afterwards.

Versions
++++++++

Check if semantic versioning applies.

- ``Products.CMFPlone`` - it is a feature and goes into 5.1, ok.
- ``plone.namedfile`` - version must be increased on minor level, since this is a feature added.
- ``plone.app.upgrade`` - ok
- ``plone.app.portlets`` - version must be increased on minor level, since this is a feature added.
- ``plone.app.contenttypes`` - version must be increased on minor level, since this is a feature added.
- ``documentation``  - it is a feature and goes into 5.1 docs, ok.


Documentation
+++++++++++++

Documentation was written and looks good!


Conclusion
----------

I propose to merge this PLIP into the 5.1 series after versions on the single packages are increased.
