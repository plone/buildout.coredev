#!/bin/bash

# Run this in the src/ directory to add the Dexterity packages as
# svn externals.

echo 'Adding dexterity externals...'
svn propget svn:externals . > EXTERNALS.txt
svn propget svn:externals https://svn.plone.org/svn/plone/plone.dexterity/buildouts/dev/src >> EXTERNALS.txt
svn propset svn:externals -F EXTERNALS.txt .
svn up
