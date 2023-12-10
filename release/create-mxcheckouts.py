# -*- coding: utf-8 -*-
"""Parse checkouts from a buildout configuration and write to a mxdev
compatible ini file.

This script is called by 'tox -c release/tox.ini -e create-mxcheckouts.py'

Manual usage: bin/python create-mxcheckouts.py
"""

# From: create-constraints.py

import os
import sys

from zc.buildout import buildout

if not len(sys.argv) == 3:
    print("ERROR. Usage: create-mxcheckouts.py buildout.cfg checkouts.ini")
    sys.exit(1)
config_file = sys.argv[1]
config_file = os.path.realpath(config_file)
checkouts_file = sys.argv[2]
checkouts_file = os.path.realpath(os.path.join(os.getcwd(), checkouts_file))
config = buildout.Buildout(config_file, [])

checkouts = config.get("buildout", {}).get("auto-checkout", "").split("\n")

with open(checkouts_file, "w") as cfile:
    cfile.write(f"# File created by {os.path.relpath(__file__)}\n")
    cfile.write(f"# Parsed from {os.path.relpath(config_file)}\n")

    # Set default to not checkout any sources.
    cfile.write("\n[settings]\n")
    cfile.write("default-use = false\n")

    cfile.write("\n")
    for name in sorted(checkouts, key=lambda x: x.lower()):
        cfile.write(f"\n[{name}]\n")
        cfile.write("use = true\n")

print(f"Wrote all checkouts to {os.path.relpath(checkouts_file)}")
