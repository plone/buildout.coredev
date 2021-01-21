# -*- coding: utf-8 -*-
"""
Parse versions from buildout.cfg and write them into constraints.txt.
This script is automatically called by buildout.

Manual usage: bin/python create-constraints.py
zc.buildout needs to be importable in that python.
"""
import sys
from zc.buildout import buildout


# We could read a buildout config filename from the command line arguments,
# but for now it is fine to hardcode it:
if len(sys.argv) > 1:
    configfile = sys.argv[1] 
else:
    configfile = "buildout.cfg"

config = buildout.Buildout(configfile, [])

# Get the constraints from the version pins.
# Nice: the versions get set directly on the config.
# Note: this works like a dictionary, but is a class 'zc.buildout.buildout.Options'.
versions = config.versions
if len(sys.argv) > 2:
    constraints_file = sys.argv[1]
else:
    constraints_file = "constraints.txt"
with open(constraints_file, "w") as cfile:
    cfile.write("# File created by {}\n".format(__file__))
    cfile.write("# Constraints parsed from {}\n".format(configfile))
    for package, version in sorted(versions.items()):
        cfile.write("{}=={}\n".format(package, version))
print("Wrote all versions as constraints to {}.".format(constraints_file))
