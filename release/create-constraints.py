# -*- coding: utf-8 -*-
"""Parse versions from buildout.cfg and write them into constraints.txt.

This script is called by 'tox -c release/tox.ini -e constraints'

It only needs to work in Python 3.

Manual usage: bin/python create-constraints.py
zc.buildout needs to be importable in that python.
"""
from zc.buildout import buildout

import os
import sys


# List packages that we should not include.
# Originally this was for packages that are pinned by Zope
# but cannot be pip installed on Py 2 or on Py 3.
DENYLIST = [
]

# We could hardcode paths here, but working directories in tox confuse me.
if not len(sys.argv) == 3:
    print("ERROR. Usage: create-constraints.py buildout.cfg constraints.txt")
    sys.exit(1)
config_file = sys.argv[1]
config_file = os.path.realpath(config_file)
constraints_file = sys.argv[2]
constraints_file = os.path.realpath(os.path.join(os.getcwd(), constraints_file))
config = buildout.Buildout(config_file, [])

# Get the constraints from the version pins.
# Nice: the versions get set directly on the config.
# Note: this works like a dictionary, but is a class 'zc.buildout.buildout.Options'.
versions = config.versions

with open(constraints_file, "w") as cfile:
    cfile.write("# File created by {}\n".format(__file__))
    cfile.write("# Constraints parsed from {}\n".format(config_file))
    cfile.write("# In pre alpha stage we need a find-links, to find internal non-PyPI releases.\n")
    cfile.write("-f https://dist.plone.org/release/6.0-dev/\n")
    for package, version in sorted(versions.items()):
        if package in DENYLIST:
            print("Ignoring blacklisted package {}".format(package))
            continue
        cfile.write("{}=={}\n".format(package, version))

print("Wrote all versions as constraints to {}".format(constraints_file))
