# -*- coding: utf-8 -*-
"""Combine constraints2.txt and constraints3.txt into constraints.txt.

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
constraints36 = os.path.join(directory, "constraints36.txt")
constraints37 = os.path.join(directory, "constraints37.txt")
constraints38 = os.path.join(directory, "constraints38.txt")
constraints2 = os.path.join(directory, "constraints2.txt")
for filename in (constraints2, constraints36, constraints37, constraints38):
    if not os.path.exists(filename):
        print(f"ERROR: {filename} does not exist.")
        print("Run: tox -p auto -e constraints2,constraints36,constraints37,constraints38,constraints")
        sys.exit(1)

c2 = parse_file(constraints2)
c36 = parse_file(constraints36)
c37 = parse_file(constraints37)
c38 = parse_file(constraints38)

# Gather them all in one dictionary.
pins = defaultdict(dict)
for package, version in c2.items():
    pins[package][2] = version
for package, version in c36.items():
    pins[package][36] = version
for package, version in c37.items():
    pins[package][37] = version
for package, version in c38.items():
    pins[package][38] = version

# Combine them.
combi = []
for package, versions in pins.items():
    py2_version = versions.pop(2, None)
    if not versions:
        # Python 2 only
        combi.append(f'{package}=={py2_version}; python_version < "3.0"')
        continue
    py36_version = versions.pop(36, None)
    if py2_version == py36_version:
        # Python 2 and 3 have same version pin.
        combi.append(f"{package}=={py2_version}")
        continue
    # Python 2 and 3 have different version pin.
    # Add both, starting with Python 2.
    if py2_version is not None:
        combi.append(f'{package}=={py2_version}; python_version < "3.0"')
    # But 36, 37 and 38 may still have differences.
    py37_version = versions.pop(37, None)
    py38_version = versions.pop(38, None)
    if py36_version == py37_version == py38_version:
        # All Py3 versions are the same.
        combi.append(f'{package}=={py36_version}; python_version >= "3.0"')
        continue
    # 36, 37 and 38 have differences.
    if py36_version != py37_version:
        combi.append(f'{package}=={py36_version}; python_version == "3.6"')
    if py37_version == py38_version:
        combi.append(f'{package}=={py37_version}; python_version > "3.6"')
        continue
    combi.append(f'{package}=={py37_version}; python_version == "3.7"')
    combi.append(f'{package}=={py38_version}; python_version == "3.8"')

with open(constraints, "w") as myfile:
    myfile.write("\n".join(combi) + "\n")
print(f"Wrote combined Python 2 and 3 constraints to {constraints}.")
