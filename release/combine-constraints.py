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
constraints39 = os.path.join(directory, "constraints39.txt")
constraints310 = os.path.join(directory, "constraints310.txt")
for filename in (constraints38, constraints39, constraints310):
    if not os.path.exists(filename):
        print(f"ERROR: {filename} does not exist.")
        print(
            "Run: tox -p auto -e constraints2,constraints38,constraints39,constraints310,constraints"
        )
        sys.exit(1)

c38 = parse_file(constraints38)
c39 = parse_file(constraints39)
c310 = parse_file(constraints310)

# Gather them all in one dictionary.
pins = defaultdict(dict)
for package, version in c38.items():
    pins[package][38] = version
for package, version in c39.items():
    pins[package][39] = version
for package, version in c310.items():
    pins[package][310] = version

# Combine them.
combi = []
for package, versions in pins.items():
    py38_version = versions.pop(38, None)
    py39_version = versions.pop(39, None)
    py310_version = versions.pop(310, None)
    if py38_version == py39_version == py310_version:
        # All versions are the same.
        combi.append(f"{package}=={py310_version}")
        continue
    # Some versions are different or missing.
    # Start with the lowest Python.
    if py38_version == py39_version == py310_version:
        # All higher Python versions are the same.
        combi.append(f'{package}=={py38_version}; python_version >= "3.8"')
        continue
    if py38_version is not None:
        combi.append(f'{package}=={py38_version}; python_version == "3.8"')
    if py39_version == py310_version and py39_version is not None:
        combi.append(f'{package}=={py39_version}; python_version >= "3.9"')
        continue
    if py39_version is not None:
        combi.append(f'{package}=={py39_version}; python_version == "3.9"')
    if py310_version is not None:
        combi.append(f'{package}=={py310_version}; python_version >= "3.10"')

output = "\n".join(combi) + "\n"
# sanity check:
assert "==None" not in output
with open(constraints, "w") as myfile:
    myfile.write(output)
print(f"Wrote combined constraints for all Python versions to {constraints}.")
