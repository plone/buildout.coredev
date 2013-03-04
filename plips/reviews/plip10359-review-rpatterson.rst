PLIP 10359: Convert control panels to use z3c.form
==============================================

PLIP ticket: https://dev.plone.org/ticket/10359

Review by Ross Patterson (me@rpatterson.net, zenwryly@irc.freenode.net)

The PLIP was reviewed on Ubuntu 12.04 using python 2.7.3 and Chromium 27.


Review steps
------------

- Set up the buildout using the PLIP's config::

  $ bin/buildout -c plips/plip10359-z3cform-controlpanel.cfg -N

TODO

- Ran tests for the PLIP's auto-checkout packages::

  $ bin/test -s plone.app.controlpanel -s plone.app.discussion -s plone.app.registry
  $ bin/test -s Products.CMFPlone

- Reviewed the code changes the PLIP's auto-checkout packages

Notes and observations
----------------------

Tests wouldn't run under newest versions in coredev 4.3::

    Running tests at level 1
    Running plone.app.controlpanel.testing.PloneAppControlpanel:Functional tests:
      Set up plone.testing.zca.LayerCleanup in 0.000 seconds.
      Set up plone.testing.z2.Startup in 0.123 seconds.
      Set up plone.app.testing.layers.PloneFixture Traceback (most recent call last):
      File "/opt/src/eggs/zope.testing-3.9.7-py2.7.egg/zope/testing/testrunner/runner.py", line 366, in run_layer
        setup_layer(options, layer, setup_layers)
      File "/opt/src/eggs/zope.testing-3.9.7-py2.7.egg/zope/testing/testrunner/runner.py", line 628, in setup_layer
        setup_layer(options, base, setup_layers)
      File "/opt/src/eggs/zope.testing-3.9.7-py2.7.egg/zope/testing/testrunner/runner.py", line 628, in setup_layer
        setup_layer(options, base, setup_layers)
      File "/opt/src/eggs/zope.testing-3.9.7-py2.7.egg/zope/testing/testrunner/runner.py", line 633, in setup_layer
        layer.setUp()
      File "/opt/src/buildout.coredev/src/plone.app.testing/plone/app/testing/layers.py", line 100, in setUp
        self.setUpZCML()
      File "/opt/src/buildout.coredev/src/plone.app.testing/plone/app/testing/layers.py", line 160, in setUpZCML
        loadAll('configure.zcml')
      File "/opt/src/buildout.coredev/src/plone.app.testing/plone/app/testing/layers.py", line 155, in loadAll
        xmlconfig.file(filename, package, context=context)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 649, in file
        include(context, name, package)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 548, in include
        processxmlfile(f, context)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 380, in processxmlfile
        parser.parse(src)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 107, in parse
        xmlreader.IncrementalParser.parse(self, source)
      File "/usr/lib/python2.7/xml/sax/xmlreader.py", line 123, in parse
        self.feed(buffer)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 207, in feed
        self._parser.Parse(data, isFinal)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 349, in end_element_ns
        self._cont_handler.endElementNS(pair, None)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 359, in endElementNS
        self.context.end()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 558, in end
        self.stack.pop().finish()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 706, in finish
        actions = self.handler(context, **args)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 548, in include
        processxmlfile(f, context)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 380, in processxmlfile
        parser.parse(src)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 107, in parse
        xmlreader.IncrementalParser.parse(self, source)
      File "/usr/lib/python2.7/xml/sax/xmlreader.py", line 123, in parse
        self.feed(buffer)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 207, in feed
        self._parser.Parse(data, isFinal)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 349, in end_element_ns
        self._cont_handler.endElementNS(pair, None)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 359, in endElementNS
        self.context.end()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 558, in end
        self.stack.pop().finish()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 706, in finish
        actions = self.handler(context, **args)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 548, in include
        processxmlfile(f, context)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 380, in processxmlfile
        parser.parse(src)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 107, in parse
        xmlreader.IncrementalParser.parse(self, source)
      File "/usr/lib/python2.7/xml/sax/xmlreader.py", line 123, in parse
        self.feed(buffer)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 207, in feed
        self._parser.Parse(data, isFinal)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 349, in end_element_ns
        self._cont_handler.endElementNS(pair, None)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 359, in endElementNS
        self.context.end()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 558, in end
        self.stack.pop().finish()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 706, in finish
        actions = self.handler(context, **args)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 548, in include
        processxmlfile(f, context)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 380, in processxmlfile
        parser.parse(src)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 107, in parse
        xmlreader.IncrementalParser.parse(self, source)
      File "/usr/lib/python2.7/xml/sax/xmlreader.py", line 123, in parse
        self.feed(buffer)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 207, in feed
        self._parser.Parse(data, isFinal)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 349, in end_element_ns
        self._cont_handler.endElementNS(pair, None)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 359, in endElementNS
        self.context.end()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 558, in end
        self.stack.pop().finish()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 706, in finish
        actions = self.handler(context, **args)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 548, in include
        processxmlfile(f, context)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 380, in processxmlfile
        parser.parse(src)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 107, in parse
        xmlreader.IncrementalParser.parse(self, source)
      File "/usr/lib/python2.7/xml/sax/xmlreader.py", line 123, in parse
        self.feed(buffer)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 207, in feed
        self._parser.Parse(data, isFinal)
      File "/usr/lib/python2.7/xml/sax/expatreader.py", line 349, in end_element_ns
        self._cont_handler.endElementNS(pair, None)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/xmlconfig.py", line 359, in endElementNS
        self.context.end()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 558, in end
        self.stack.pop().finish()
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 705, in finish
        args = toargs(context, *self.argdata)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 1397, in toargs
        args[str(name)] = field.fromUnicode(s)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/fields.py", line 137, in fromUnicode
        value = self.context.resolve(name)
      File "/opt/src/eggs/zope.configuration-3.7.4-py2.7.egg/zope/configuration/config.py", line 179, in resolve
        mod = __import__(mname, *_import_chickens)
      File "/opt/src/eggs/plone.app.theming-1.1b2-py2.7.egg/plone/app/theming/browser/controlpanel.py", line 31, in <module>
        from plone.app.controlpanel.skins import ISkinsSchema
    ZopeXMLConfigurationError: File "/opt/src/buildout.coredev/src/Products.CMFPlone/Products/CMFPlone/configure.zcml", line 31.2-31.41
        ZopeXMLConfigurationError: File "/opt/src/buildout.coredev/src/plone.app.upgrade/plone/app/upgrade/configure.zcml", line 14.4-14.30
        ZopeXMLConfigurationError: File "/opt/src/buildout.coredev/src/plone.app.upgrade/plone/app/upgrade/v43/configure.zcml", line 7.4-7.88
        ZopeXMLConfigurationError: File "/opt/src/eggs/plone.app.theming-1.1b2-py2.7.egg/plone/app/theming/configure.zcml", line 22.4-22.34
        ZopeXMLConfigurationError: File "/opt/src/eggs/plone.app.theming-1.1b2-py2.7.egg/plone/app/theming/browser/configure.zcml", line 17.4-23.10
        ImportError: No module named skins


Conclusion
----------
