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

- Ran single tests for the PLIP's auto-checkout packages::

  $ test -s Products.CMFCore
  $ test -s Products.Archetypes
  $ test -s Products.CMFPlone
  $ test -s plone.app.content
  $ test -s plone.app.upgrade
  $ test -s Products.CMFEditions
  $ test -s Products.ATContentTypes
  $ test -s Products.CMFUid
  $ test -s plone.app.blob

- combined PLIP test at http://jenkins.plone.org/view/PLIPs/job/plip-collective-indexing/2/

- Reviewed code

- Manual testing TTW


Notes and observations
----------------------

Automated testing
+++++++++++++++++

- tests of jenkins job are ?green/red.
- tests of ``Products.CMFCore`` are passing.
- tests of ``Products.Archetypes`` are passing.
- tests of ``Products.CMFPlone`` are passing.
- tests of ``plone.app.content`` are passing.
- tests of ``plone.app.upgrade`` are passing.
- tests of ``Products.CMFEditions`` are passing.
- tests of ``Products.ATContentTypes`` are passing.
- tests of ``Products.CMFUid`` are passing.
- tests of ``plone.app.blob`` are passing.
- combined PLIP test job passes on jenkins.

The PLIP job clones ``collective.indexing``, it is not included in the test runner.
At first this is confusing, but it is for end of life, so including it does not make sense at all.


Manual testing
++++++++++++++

Hence the PLIP does not involve UI specific parts, manual testing does not make much sense.


Code review
+++++++++++

The code is overall very clean, follows our guidelines and is well structured.
Cleanups of the underlying codebase were all done before on separate Pull Requests.
Naming is expressive and OK, but it is partly old style,
Hence the code was added to existing naming of the same style this is fine.


Versions
++++++++

Check if semantic versioning applies.

- ``Products.CMFCore`` well, on a branch, difficult with CMFCore handling overall.
  In fact the current way to deal with it is wrong.
  Its complicated.
  But thats for the release team.
- ``Products.Archetypes`` 1.11.4 -> 1.11.5 NOT ok, more than a bugfix release here.
  At least minor increase needed imo.
- ``Products.CMFPlone`` 5.0 to 5.1, OK feature change
- ``plone.app.content`` tests changes only. bugfix level OK.
- ``plone.app.upgrade``  tests changes only. bugfix level OK.
- ``Products.CMFEditions`` tests changes only. bugfix level OK.
- ``Products.ATContentTypes`` tests changes only. bugfix level OK.
- ``Products.CMFUid`` tests changes only. bugfix level OK.
- ``plone.app.blob`` tests changes only. bugfix level OK.
- ``collective.indexing`` was released as 2.0b1 at 2013-02-16.
  The recent changes are removing the patches and removes the merged parts,
  so this should go into a major version 3.0 change, because it was beta already.


Documentation
+++++++++++++

Documentation is missing. As stated in the PLIP we need to

- describe the new feature,
- explain how to update tests,
- explain how to migrate from ``collective.indexing`` as part of its end of life release.


Conclusion
----------

I propose to merge this PLIP.

Preferable is to write the missing documentation first.

The merge should be coordinated close with our Release Manager Eric Steele,
because ``Products.CMFCore`` is a fork in the plone organisation and he knows the process to get this upstream or how to proceed here best.
