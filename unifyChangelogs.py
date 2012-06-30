#!/usr/bin/env python
# -*- coding: ascii -*-
import urllib
from distutils.version import StrictVersion
from docutils.core import publish_doctree
import sys


def pullVersions(versionsFile):
    try:
        from ordereddict import OrderedDict
        packageVersions = OrderedDict()
    except ImportError:
        print "Unable to find OrderedDict"
        packageVersions = {}
    for line in versionsFile:
        line = line.strip().replace(" ", "")
        if line and not (line.startswith('#') or line.startswith('[')):
            try:
                package, version = line.split("=")
                version = StrictVersion(version)
            except ValueError:
                pass
            else:
                packageVersions[package] = version
    return packageVersions


def getSourceLocation(packageName):
    from ConfigParser import RawConfigParser
    import re
    config = RawConfigParser()
    config.read('sources.cfg')

    if config.has_option('sources', packageName):
        sourceLine = config.get('sources', packageName)

        _template_split = re.compile('([$]{[^}]*})').split
        # _simple = re.compile('[-a-zA-Z0-9 ._]+$').match

        value = _template_split(sourceLine)
        if len(value) == 1:
            url = value[0].split()[1]
        else:
            variable = value[1][2:-1].split()[0].split(':')
            
            section, option = variable
            value[1] = config.get(section, option)
            url = ''.join(value[1:])
            url = url.split(' pushurl')[0]

        url = url.replace('git:', 'https:')
        url = url.replace('.git', '')
        return url
    # sources = {}
    # for line in sourcesFile:
    #     line = line.strip().replace(" ","")
    #     for t in ['svn','git']:
    #         line = line.replace("=%s" % t,";;")

    #     if line and not (line.startswith('#') or line.startswith('[')):
    #         try:
    #             package, location = line.split(";;")
    #             sources[package] = location
    #         except ValueError:
    #             print line
    return ""


def main(argv):
    priorVersionNumber = sys.argv[1]
    currentVersionNumber = sys.argv[2]

    dist_url = "http://dist.plone.org/release/%s/versions.cfg"
    priorVersionsFile = urllib.urlopen(dist_url % priorVersionNumber)
    priorVersions = pullVersions(priorVersionsFile)

    currentVersionsFile = urllib.urlopen(dist_url % currentVersionNumber)
    currentVersions = pullVersions(currentVersionsFile)

    # sourcesFile = open("sources.cfg", "r")
    # sources = pullSources #pullSources(sourcesFile)
    outputStr = ""
    for package, version in currentVersions.iteritems():
        if package in priorVersions:
            priorVersion = priorVersions[package]
            if version > priorVersion:
                packageChange = u"%s: %s %s %s" % (package, priorVersion, u"\u2192", version)
                outputStr += u"\n" + packageChange + u"\n" + u"-" * len(packageChange) + "\n"
            
                source = getSourceLocation(package)
                if source:
                    if 'github' in source:
                        source = source.replace(' branch=', '/raw/')
                        # https://github.com/plone/Plone/raw/4.1/README.txt
                        paths_to_try = ["raw/master/CHANGES.txt",
                                        "raw/master/CHANGES.rst",
                                        "raw/master/docs/HISTORY.txt",
                                        "raw/master/docs/CHANGES.txt"]
                    else:
                        paths_to_try = ["/CHANGES.txt",
                                        "/docs/CHANGES.txt",
                                        "/docs/HISTORY.txt",
                                        "/docs/CHANGES.rst"]
                        try:
                            paths_to_try.append('/%s/CHANGES.txt' % '/'.join(package.split('.')))
                        except:
                            pass
                    # if 'theming' in package or 'imaging' in package:
                    #     import pdb; pdb.set_trace( )

                    for structure in paths_to_try:
                        url = "%s/%s" % (source, structure)
                        try:
                            response = urllib.urlopen(url)
                        except IOError:
                            print "Unable to reach %s" % url
                        else:
                            if response.code == 200:
                                logtext = response.read()
                                tree = publish_doctree(logtext)

                                def isValidVersionSection(x):
                                    if x.tagname == "section":
                                        try:
                                            logVersion = StrictVersion(x['names'][0].split()[0])
                                        except (ValueError, IndexError):
                                            pass
                                        else:
                                            return logVersion > priorVersion and logVersion <= version
                                    return False
             
                                foundSections = tree.traverse(condition=isValidVersionSection)
                                if foundSections:
                                    outputStr += u"\n"
                                    for s in foundSections:
                                        s.children[-1]
                                        childlist = s.children[-1]
                                        bullet = "- "
                                        for child in childlist.children:
                                            text = child.astext()
                                            text = text.replace("\n","\n" + " " * len(bullet))
                                            outputStr += bullet + text + u"\n"

                                break
    
    print outputStr


if __name__ == "__main__":
    main(sys.argv[1:])
