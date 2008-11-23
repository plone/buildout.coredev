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

  ./bin/instance

  or

  ./bin/paster serve etc/plone.ini

Adding a new user (`./bin/instance adduser user password`):

  ./bin/addzope2user user password

A debug prompt (`./bin/instance debug`):

  ./bin/debugzope2

Running tests (`./bin/instance test -v -s plone.i18n`):

  ./bin/test -v -s plone.i18n
