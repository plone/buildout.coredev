#!/bin/bash

# Run this in the root buildout directory to add the Dexterity packages as
# svn externals.

echo 'Adding dexterity externals...'
svn propget svn:externals src > EXTERNALS.txt
svn propget svn:externals https://svn.plone.org/svn/plone/plone.dexterity/buildouts/dev/src >> EXTERNALS.txt
echo 'z3c.form http://svn.zope.org/repos/main/z3c.form/trunk' >> EXTERNALS.txt
svn propset svn:externals -F EXTERNALS.txt src
svn up
