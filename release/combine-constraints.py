# -*- coding: utf-8 -*-
"""Combine all constraints*.txt into one constraints.txt.

See tox.ini.
This is Python 3 only.
"""
from collections import defaultdict

import os
import sys


if not len(sys.argv) == 2:
    print("ERROR. Usage: combine-constraints.py <directory with contraints files>")
    sys.exit(1)
directory = sys.argv[1]


def parse_file(filename):
    mapping = {}
    with open(filename) as myfile:
        for line in myfile.read().splitlines():
            if "==" not in line:
                continue
            package, version = line.split("==")
            mapping[package] = version
    return mapping


constraints = os.path.join(directory, "constraints.txt")
constraints38 = os.path.join(directory, "constraints38.txt")
constraints2 = os.path.join(directory, "constraints2.txt")
for filename in (constraints2, constraints38):
    if not os.path.exists(filename):
        print(f"ERROR: {filename} does not exist.")
        print(
            "Run: tox -p auto -e constraints2,constraints38,constraints"
        )
        sys.exit(1)

c2 = parse_file(constraints2)
c38 = parse_file(constraints38)

# Gather them all in one dictionary.
pins = defaultdict(dict)
for package, version in c2.items():
    pins[package][2] = version
for package, version in c38.items():
    pins[package][38] = version

# Combine them.
combi = []
for package, versions in pins.items():
    py2_version = versions.pop(2, None)
    py38_version = versions.pop(38, None)
    if py2_version == py38_version:
        # All versions are the same.
        combi.append(f"{package}=={py2_version}")
        continue
    # Some versions are different or missing.
    # Start with Python 2.
    if py2_version is not None:
        combi.append(f'{package}=={py2_version}; python_version < "3.0"')
    if py38_version is not None:
        combi.append(f'{package}=={py38_version}; python_version >= "3.0"')

output = "\n".join(combi) + "\n"
# sanity check:
assert "==None" not in output
with open(constraints, "w") as myfile:
    myfile.write(output)
print(f"Wrote combined constraints for all Python versions to {constraints}.")
