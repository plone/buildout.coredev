#!/usr/bin/env bash
#
# This script is called by `make test`. This is when using pip-installed Plone.
# If you are using Buildout, you can use the bin/test command instead.

set -e

# Make sure these variables exist in the script, whether they are passed via
# 'make test' or the OS environment, or not at all.
TEST_ARGS="${TEST_ARGS}"
TEST_PACKAGE="${TEST_PACKAGE}"

if [ -z "$TEST_ARGS" ] && [ -z "$TEST_PACKAGE" ]; then
    echo """
** Running ALL tests (except robot) for the PRE-DEFINED packages. **

You can pass test arguments with a TEST_ARGS variable.
You can specify a single test package with a TEST_PACKAGE variable.
This can be an environment variable or you pass it to 'make test'.
For example:

make test TEST_ARGS=--all TEST_PACKAGE=plone.app.discussion

For more control call $0 directly and pass arguments for zope-testrunner.
"""
fi

# PACKAGES are manually copied and then adapted from test-eggs in tests.cfg.
# The [test] extras should not be here.
# Please keep these lists in sync.
PACKAGES="""
borg.localrole
collective.monkeypatcher
diazo
five.customerize
five.intid
plone.alterego
plone.api
plone.app.caching
plone.app.content
plone.app.contentlisting
plone.app.contentmenu
plone.app.contentrules
plone.app.contenttypes
plone.app.customerize
plone.app.dexterity
plone.app.discussion
plone.app.event
plone.app.i18n
plone.app.intid
plone.app.iterate
plone.app.layout
plone.app.linkintegrity
plone.app.locales
plone.app.lockingbehavior
plone.app.multilingual
plone.app.portlets
plone.app.querystring
plone.app.redirector
plone.app.registry
plone.app.relationfield
plone.app.robotframework
plone.app.testing
plone.app.textfield
plone.app.theming
plone.app.upgrade
plone.app.users
plone.app.uuid
plone.app.versioningbehavior
plone.app.viewletmanager
plone.app.vocabularies
plone.app.widgets
plone.app.workflow
plone.app.z3cform
plone.autoform
plone.batching
plone.behavior
plone.base
plone.browserlayer
plone.cachepurging
plone.caching
plone.classicui
plone.contentrules
plone.dexterity
plone.distribution
plone.event
plone.exportimport
plone.folder
plone.formwidget.namedfile
plone.i18n
plone.indexer
plone.intelligenttext
plone.keyring
plone.locking
plone.memoize
plone.namedfile
plone.outputfilters
plone.portlet.collection
plone.portlet.static
plone.portlets
plone.protect
plone.registry
plone.resource
plone.resourceeditor
plone.rest
plone.restapi
plone.rfc822
plone.scale
plone.schema
plone.schemaeditor
plone.session
plone.staticresources
plone.stringinterp
plone.subrequest
plone.supermodel
plone.testing
plone.theme
plone.transformchain
plone.uuid
plone.volto
plone.z3cform
plonetheme.barceloneta
Products.CMFDiffTool
Products.CMFDynamicViewFTI
Products.CMFEditions
Products.CMFPlacefulWorkflow
Products.CMFPlone
Products.CMFUid
Products.DateRecurringIndex
Products.DCWorkflow
Products.ExtendedPathIndex
Products.GenericSetup
Products.isurlinportal
Products.MimetypesRegistry
Products.PlonePAS
Products.PluggableAuthService
Products.PluginRegistry
Products.PortalTransforms
Products.statusmessages
Products.ZopeVersionControl
repoze.xmliter
"""

if [[ "$TEST_ARGS" == *"--all"* ]]; then
    echo """Running robot tests, if they are there, due to TEST_ARGS=\"${TEST_ARGS}\"
You are responsible for initializing the robotframework browser first.
If you want to run *only* robot test of a package, do something like this:

.venv/bin/rfbrowser init
export ROBOTSUITE_PREFIX=ONLYROBOT
make test TEST_ARGS=\"-t ONLYROBOT --all\" TEST_PACKAGE=plone.app.discussion
"""
fi

if [ -z "$TEST_PACKAGE" ]; then
    for package in $PACKAGES; do
      TEST_ARGS="$TEST_ARGS -s $package"
    done
else
    TEST_ARGS="$TEST_ARGS -s $TEST_PACKAGE"
fi

# Note: the --auto-path requires zope.testrunner 7.4 or higher.
CMD="zope-testrunner --auto-color --auto-progress --auto-path $TEST_ARGS"
echo "Running $CMD"

# In most cases we can call $CMD directly.
# But when you have quotes within quotes, 'eval' helps.  For example:
# make test TEST_ARGS='--all -t "Add a fieldSet and move a field into this fieldset"'
eval $CMD

exit 0
