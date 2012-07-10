#!/usr/bin/env python
# -*- coding: ascii -*-
import urllib
from distutils.version import StrictVersion
from docutils.core import publish_doctree
import sys

dist_url = "http://dist.plone.org/release/%s/versions.cfg"


def pullVersions(versionNumber):
    try:
        from ordereddict import OrderedDict
        packageVersions = OrderedDict()
    except ImportError:
        print "Unable to find OrderedDict"
        packageVersions = {}
    url = dist_url % versionNumber
    versionsFile = urllib.urlopen(url)
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
    print "Parsed %s" % url
    return packageVersions


def getSourceLocation(packageName):
    from ConfigParser import RawConfigParser
    import re
    config = RawConfigParser()
    config.read('sources.cfg')

    if config.has_option('sources', packageName):
        sourceLine = config.get('sources', packageName)
        branch = "master"
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

            branch_check = sourceLine.split('branch=')
            if len(branch_check) == 2:
                branch = branch_check[-1]
        url = url.replace('git:', 'https:')
        url = url.replace('.git', '')
        return url, branch
    return "", ""


def main(argv):
    priorVersionNumber = sys.argv[1]
    currentVersionNumber = sys.argv[2]

    priorVersions = pullVersions(priorVersionNumber)
    currentVersions = pullVersions(currentVersionNumber)

    outputStr = ""
    for package, version in currentVersions.iteritems():
        if package in priorVersions:
            priorVersion = priorVersions[package]
            if version > priorVersion:
                print "%s has a newer version" % package
                packageChange = u"%s: %s %s %s" % (package, priorVersion, u"\u2192", version)
                outputStr += u"\n" + packageChange + u"\n" + u"-" * len(packageChange) + "\n"
                source, branch = getSourceLocation(package)
                if source:
                    if 'github' in source:
                        # source = source.replace(' branch=', '/raw/')
                        # https://github.com/plone/Plone/raw/4.1/README.txt
                        paths_to_try = ["raw/%s/CHANGES.txt" % branch,
                                        "raw/%s/CHANGES.rst" % branch,
                                        "raw/%s/docs/HISTORY.txt" % branch,
                                        "raw/%s/docs/CHANGES.txt" % branch]
                    else:
                        paths_to_try = ["/CHANGES.txt",
                                        "/docs/CHANGES.txt",
                                        "/docs/HISTORY.txt",
                                        "/docs/CHANGES.rst"]
                        try:
                            paths_to_try.append('/%s/CHANGES.txt' % '/'.join(package.split('.')))
                        except:
                            pass

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
