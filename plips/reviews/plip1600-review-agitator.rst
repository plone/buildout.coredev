
PLIP: Easily change default search order #1600
==============================================

PLIP ticket: https://github.com/plone/Products.CMFPlone/issues/1600

Review by Peter Holzer (peter.holzer@agitator.com)

The PLIP was reviewed on OSX 10.11.6 using python 2.7.12 and Firefox 49.0.1.

October 3, 2016


Review steps
------------

- Set up the buildout using the PLIP's config::

  $ ./bin/buildout -c plips/plip-1600.cfg


- Manual testing TTW with Plone 5.1

  - Created new site 
  
  - Uploaded various PDFs over several minutes
  
  - Tested header search viewlet default/relevance is working as we know it, hitting return and viewing the search result on @@search shows the same result order
  
  - Switching to sort_on date via @@search-controlpanel
  
  - Search viewlet shows order according to upload/last-modified date, hitting return and viewing the search result on @@search shows the same result order starting with the last modified as first item
  
  - Switching to sort_on alphabetically via @@search-controlpanel
  
  - Search viewlet shows order alphabetically, hitting return and viewing the search result on @@search shows the same result order starting with bill-2015-10-10 and continuing with bill-2015-11-10 and bill-2015-12-10
  
  - added search portlet
  
  - repeated ttw tests, same result



-  Manual testing of upgrade step on an existing site with coredev 5.1

  - manually applying upgrade steps "Run to51beta1 upgrade profile" & "Add default search options"
  
  - upgrade step did create the control panel entry


Notes and observations
----------------------

Testing
-------

- Results as described in the PLIP
- Upgrade step works and did create control panel property on existing site

Conclusion
----------

- All things work as expected

