PLIP 1653: Restructure CMFPlone static resources
================================================

PLIP ticket
    https://github.com/plone/Products.CMFPlone/issues/1653

Review by
    Alessandro Pisa (alessandro.pisa@gmail.com)

Environment
    The PLIP was reviewed using:

    - Kubuntu 18.10 64-bitusing
    - Python 2.7.15
    - Chrome 70.0.3538.110 (64-bit)
    - yarn 1.12.3

Date
    November 26, 2018


Jenkins jobs
------------

The plip buildout jobs work good:

- https://jenkins.plone.org/view/PLIPs/job/plip-plone-staticresources-2.7/
- https://jenkins.plone.org/view/PLIPs/job/plip-plone-staticresources-3.6/
- https://jenkins.plone.org/view/PLIPs/job/plip-plone-staticresources-3.7/


PLIP buildout
-------------

- Set up the buildout using the PLIP's config::

  $ cd plips && ../bin/buildout -c plip-1653-staticresources.cfg

Works good but we have the missing pin: `profilehooks = 1.8.1`

I had to manually edit:

- parts/instance/etc/package-includes/998-resources-configure.zcml

to transform the relative path that points to the resource folder
in to an absolute one.


Involved Packages and its pull requests
---------------------------------------

- jquery.recurrenceinput.js:
  I created a simple PR
  (https://github.com/collective/jquery.recurrenceinput.js/pull/32)
  that looks like can be merged pretty soon without waiting
  for the other plip packages.
  This is checked out in the src directory even if it is not an egg.
  Unsure how it is pulled in.

- mockup:
  PR https://github.com/plone/mockup/pull/874
  had to be updated because of conflicting changes.
  Running make works until the very end but then rasises this error:
  https://github.com/plone/mockup/pull/874#issuecomment-441812390
  Browsing the docs complains about missing react.

- plone.app.theming:
  https://github.com/plone/plone.app.theming/pull/149
  Mostly removal of old resources. Looks good.

- plone.resourceeditor: https://github.com/plone/plone.resourceeditor/pull/22
  Mostly removal of old resources. Looks good.

- plone.staticresources:
  Found some issues, most of them are already resolved.
  Code looks good.
  There is still an issue compile the bundle with Python3
  (https://github.com/plone/plone.staticresources/issues/4)

- Products.CMFPlone:
  Mostly removal of old resources. Looks good.


Manual testing
++++++++++++++

I created a fresh Plone instance and browsed it checking that the styles
were properly applied and that no JavaScript console was present.

I notice that I am getting 404 when getting:
http://0.0.0.0:8080/plonejsi18n?domain=widgets&language=en_US

Still unsure if this is also a problem on current master.


Code review
+++++++++++

Code looks nice and basically it is code moved from one package to another.

Test coverage is given.


Versions
++++++++

All the packages involved have breaking changes
and will be compatible only be compatible with Plone >= 5.2.
Only jquery.recurrenceinput.js can have a feature release.

Documentation
+++++++++++++

It seems to me that the documentation has to be rechecked.

Conclusion
----------

The framework team should discuss if, given the alpha state of Plone 5.2,
this PLIP can be merged right now and apply fixes incrementally.
My wish is that at least the Makefile for mockup will work as expected.
It might be a good idea to take some time to do this in some of the sprints.
A good candidate can be the Alpine city sprint.
