=============
plone-coredev
=============

This is the buildout configuration used to develop the Plone CMS itself.

Do not use it for your own private projects. You can learn more about
buildout in the tutorial at:

http://plone.org/documentation/tutorial/buildout

--------
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
