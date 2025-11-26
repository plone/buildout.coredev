#!/usr/bin/env bash
#
# This script is called by `make test`. This is when using pip-installed Plone.
# If you are using Buildout, you can use the bin/test command instead.

set -e

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

ARG_COUNT=$#
if test $ARG_COUNT -eq 0; then
    # As proof of concept, we only run the unit tests.
    # Locally for me (Maurits) it works without '-u' as well.
    # I did not try the robot tests.
    ARGS="-u"
    for package in $PACKAGES; do
      ARGS="$ARGS -s $package"
    done
else
    ARGS=$*
fi

# Note: the --auto-path requires this zope.testrunner 7.4 or higher.
CMD="zope-testrunner --auto-color --auto-progress --auto-path $ARGS"
echo "Running $CMD"
$CMD

exit 0
