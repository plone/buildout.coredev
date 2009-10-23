Introduction
============

*plonenext* attempts to show what the next Plone release will look like
and provide convenient tools for developers to work on one or many packages
that are used by Plone.

A default plonenext instance is no different than a standard Plone buildout
and will only differ from an existing Plone release in the specific package
versions it uses. After making a checkout of plonenext you will first need
to initialize the buildout::

  $ python2.4 bootstrap.py
  Creating directory '/local/instances/plonenext/parts'.
  Creating directory '/local/instances/plonenext/eggs'.
  Creating directory '/local/instances/plonenext/develop-eggs'.
  Generated script '/local/instances/plonenext/bin/buildout'.
  $ bin/buildout
  Getting distribution for 'buildout.eggtractor'.
  Got buildout.eggtractor 0.5.
  Getting distribution for 'setuptools'.
  ...

If you want to do some work on a specific package used
by Plone you can do so through the ``develop`` tool::

  $ bin/develop plone.openid
  Checkout out plone.openid
  Removing version pin for plone.openid
  Running buildout to update instance

You will now have a plone.openid source tree in the ``src`` subdirectory
which will be used by the instance. ``develop`` will automatically use the
correct branch when making a checkout.

::

 *Caveat*: even though the version pin for a package may be removed by the
 ``develop`` tool buildout may still choose not to use the source tree in
 ``src`` if it does not satisfy a dependency from another package.

Once you are done with your work on a package you switch back to the
standard tree using the ``undevelop`` tool:

  $ bin/undevelop plone.openid
  Removing plone.openid source tree
  Restoring version pin for plone.openid
  Running buildout to update instance


Both ``develop`` and ``undevelop`` commands accept the standard `-h` and
``--help`` options to ask for detailed usage information.


Plone development workflow
==========================

Future Plone releases will be based on the version information in the
``etc/versions`` file. The information from that file will be combined
the information in ``versions.cfg`` when a development package is added
or removed: missing entries in ``versions.cfg`` are added, and entries for
packages in ``src/`` are automatically removed.


Tips and tricks
===============

* It is not always necessary to spell out the full package name: both
  ``develop`` and ``undevelop`` will look for unique substring matches.
  So you can use *Resou* instead of *Products.ResourceRegistries*.

Frequently Asked Questions
==========================

Why use a local eggs directory?
-------------------------------

The goal of plonenext is to provide a convenient way to test what a next
Plone release will look like. All too often the presence of eggs in a
buildout download or egg cache will influence this. The use of version
pins throughout plonenext is one way to prevent that. Using a local
eggs directory which can easily be emptied to simulate installation on a
new system is another way of doing that.

