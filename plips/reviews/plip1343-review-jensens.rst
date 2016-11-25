PLIP 1343: Assimilate collective.indexing
=========================================

PLIP ticket
    https://github.com/plone/Products.CMFPlone/issues/1343

Review by
    Jens Klein (jens@bluedynamics.com)

Environment
    The PLIP was reviewed on Ubuntu 14.04 using python 2.7.12 and Firefox 50 (64-bit).

Date
    November 25, 2016

Involved Packages and its pull requests
---------------------------------------

Plone Core

- https://github.com/plone/Products.CMFCore/pull/3
- https://github.com/plone/Products.Archetypes/pull/57
- https://github.com/plone/Products.CMFPlone/pull/1595
- https://github.com/plone/plone.app.content/pull/91
- https://github.com/plone/plone.app.upgrade/pull/75
- https://github.com/plone/Products.CMFEditions/pull/37
- https://github.com/plone/Products.ATContentTypes/pull/34
- https://github.com/plone/Products.CMFUid/pull/3
- https://github.com/plone/plone.app.blob/pull/27

Collective

- https://github.com/collective.indexing branch ``merge-to-plone-core``
- https://github.com/collective.solr branch ``collective-indexing-merged``


Review steps
------------

- Check state of jenkins job on http://jenkins.plone.org/view/PLIPs/job/plip-collective-indexing/

- Set up the buildout using the PLIP's config::

  $ ./bin/buildout -Nc plips/merge-collective-indexing.cfg

- Ran tests for the PLIP's auto-checkout packages::

  $ test -s Products.CMFCore
  $ test -s Products.Archetypes
  $ test -s Products.CMFPlone
  $ test -s plone.app.content
  $ test -s plone.app.upgrade
  $ test -s Products.CMFEditions
  $ test -s Products.ATContentTypes
  $ test -s Products.CMFUid
  $ test -s plone.app.blob

- Reviewed code

- Manual testing TTW


Notes and observations
----------------------

Automated testing
+++++++++++++++++

- tests of jenkins job are ?green/red.
- tests of ``Products.CMFCore`` are passing.
- tests of ``Products.Archetypes`` are ?passing.
- tests of ``Products.CMFPlone`` are ?passing.
- tests of ``plone.app.content`` are ?passing.
- tests of ``plone.app.upgrade`` are ?passing.
- tests of ``Products.CMFEditions`` are ?passing.
- tests of ``Products.ATContentTypes`` are ?passing.
- tests of ``Products.CMFUid`` are ?passing.
- tests of ``plone.app.blob`` are ?passing.

Manual testing
++++++++++++++

The following notes are regarding the UI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



The following notes are for when using the API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Code review
+++++++++++


Documentation
+++++++++++++


Conclusion
----------

