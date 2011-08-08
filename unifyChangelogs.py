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
        packageVersions = {}        
    for line in versionsFile:
        line = line.strip().replace(" ","")
        if line and not (line.startswith('#') or line.startswith('[')):
            try:
                package, version = line.split("=")
                version = StrictVersion(version)
            except ValueError:
                pass
            else:
                packageVersions[package] = version
    return packageVersions

def pullSources(sourcesFile):
    sources = {}
    for line in sourcesFile:
        line = line.strip().replace(" ","")
        for t in ['svn','git']:
            line = line.replace("=%s" % t,";;")

        if line and not (line.startswith('#') or line.startswith('[')):
            try:
                package, location = line.split(";;")
                sources[package] = location
            except ValueError:
                print line
    return sources


def main(argv):
    priorVersionNumber = sys.argv[1]
    currentVersionNumber = sys.argv[2]

    priorVersionsFile = urllib.urlopen('http://dist.plone.org/release/%s/versions.cfg' % priorVersionNumber)
    priorVersions = pullVersions(priorVersionsFile)

    currentVersionsFile = urllib.urlopen('http://dist.plone.org/release/%s/versions.cfg' % currentVersionNumber) 
    currentVersions = pullVersions(currentVersionsFile)

    sourcesFile = open("sources.cfg", "r")
    sources = pullSources(sourcesFile)
    outputStr = ""

    for package, version in currentVersions.iteritems():
        if package in priorVersions:
            priorVersion = priorVersions[package]
            if version > priorVersion:
            
                packageChange = u"%s: %s %s %s" % (package, priorVersion, u"\u2192", version)
                outputStr += u"\n" + packageChange + u"\n" + u"-"*len(packageChange) + "\n"
            
                if package in sources:
                    source = sources[package]
                    for structure in ["/CHANGES.txt", "/docs/CHANGES.txt", "/docs/HISTORY.txt", "raw/master/CHANGES.txt"]:
                        response = urllib.urlopen("%s/%s" % (source, structure))
                        if response.code == 200:
                            break
                    logtext = response.read()

                    tree = publish_doctree(logtext)

                    def isValidVersionSection(x):
                        if x.tagname == "section":
                            try:
                                logVersion = StrictVersion(x['names'][0].split()[0])
                            except ValueError:
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
                                text = text.replace("\n","\n" + " "*len(bullet))
                                outputStr += bullet + text + u"\n"
    
    print outputStr


if __name__ == "__main__":
    main(sys.argv[1:])