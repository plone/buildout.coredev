plone-coredev
=============

This is the buildout configuration used to develop the Plone CMS itself. This
particular buildout is used to develop Plone trunk aka. Plone future or
"TPFKAP4 - The Plone formerly known as Plone 4".

Do not use it for your own private projects. You can learn more about
buildout in the tutorial at:

http://plone.org/documentation/tutorial/buildout

This buildout requires Python 2.6. Older versions of Python do no longer work.

Commands
--------

This lists the most commonly used commands in their new form. The old
variant is included in brackets.

Starting a Plone instance (`./bin/instance fg`):

  ./bin/instance-fg

Adding a new user (`./bin/instance adduser user password`):

  ./bin/instance-adduser user password

A debug prompt (`./bin/instance debug`):

  ./bin/instance-debug

Running tests (`./bin/instance test -s plone.i18n`):

  ./bin/test -s plone.i18n

Plone Base
----------

There is an additional set of commands of the base-* form. These can be used
to run the Plone Base minimal distribution. This version does not include any
Archetypes based packages. There's currently no test function for this flavor
since most tests are functional tests relying on PloneTestCase which requires
to have a folderish content type to be available.
