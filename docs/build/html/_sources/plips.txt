PLIP Implementation
===================

Create a buildout configuration file for your plip in the 'plips' folder.
Give it a descriptive name, starting with the plip number;
'plip-1234-widget-frobbing.cfg' for example. This file will define the
branches/trunks you're working with in your PLIP. It should look something
like this:

In file plips/plip-1234-widget-frobbing.cfg...::

 [buildout]
 extends = plipbase.cfg
 auto-checkout +=
  plone.somepackage
  plone.app.someotherpackage

 [sources]
  plone.somepackage = git git://github.com/plone/plone.somepackage.git branch=plip-1234-widget-frobbing
  plone.app.someotherpackage = git git://github.com/plone/plone.app.somepackage.git branch=plip-1234-widget-frobbing

 [instance]
 eggs +=
    plone.somepackage
    plone.app.someotherpackage
 zcml +=
    plone.somepackage
    plone.app.someotherpackage

Use the same naming convention when branching existing packages, and you
should always be branching packages when working on PLIPs.
