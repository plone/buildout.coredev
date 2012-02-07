PLIP 12235: Unified Batch Implementation
========================================
Ticket: https://dev.plone.org/plone/ticket/12235

Review by Alec Mitchell (alecpm@gmail.com, alecm on irc) The PLIP was
reviewed on Mac OSX using python 2.7.2 and Google Chrome 16.0.912.77

Review Steps
------------

 - Reviewed code at https://github.com/tomgross/plone.batching

 - Reviewed code changes at http://svn.zope.org/plone.z3cform/branches/plip12234-batching

 - Reviewed code changes at https://github.com/tomgross/Products.CMFPlone

 - Reviewed code changes at https://github.com/tomgross/plone.app.content

 - Ran tests and code coverage

 - Tested folder and search batching in Plone UI with dummy content


Notes and Oberservations
------------------------

 - The refactoring looks good.

 - There's still some generic looking code for batched tables in
 plone.app.content, that now depends on plone.batching.  It may make
 sense to move that into plone.batching and make it part of the
 official API.

 - The changes in plone.app.content and plone.z3cform appear to be
   fine, and it's always nice to see code reduction/simplification.

 - This PLIP is primarily about unifying the API for a consistent
 developer experience.  As a result, accessible documentation is
 perhaps the most important deliverable; the current documentation
 falls short.

 - Test coverage on plone.batching is adequate (78% average) and all
   tests pass.  Tests pass on all modified packages.
 
Issues
------

 - The setup.py in Products.CMFPlone should declare an explicit
   dependency on plone.batching.
 
 - The deprecation of __len__ seems a little strange, since the
   PloneBatch __len__ return value is different from the BaseBatch
   __len__ (which is not considered deprecated).  The PloneBatch
   version should probably return the same attribute suggested by the
   deprecation message (i.e. ''page_size'' instead of ''length'').
   The message should also indicate what value __len__ will return in
   future updates (i.e. ''sequence_length'').  Finally, all existing
   deprecated use of len(Batch) in the Plone core codebase should be
   removed to avoid warnings.
 
 - The UI issues highlighted in eleddy's review appear to have been
   resolved.

   
Conclusion
----------

Humane documentation of the API is needed, and all deprecation
warnings need to be resolved in the core.  Other than that it is
ready, but pending that work I'm +0
