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
constraints311 = os.path.join(directory, "constraints311.txt")
constraints312 = os.path.join(directory, "constraints312.txt")
for filename in (constraints38, constraints39, constraints310, constraints311, constraints312):
    if not os.path.exists(filename):
        print(f"ERROR: {filename} does not exist.")
        print(
            "Run: tox -p auto -e constraints38,constraints39,constraints310,constraints311,constraints312,constraints"
        )
        sys.exit(1)

c38 = parse_file(constraints38)
c39 = parse_file(constraints39)
c310 = parse_file(constraints310)
c311 = parse_file(constraints311)
c312 = parse_file(constraints312)

# Gather them all in one dictionary.
pins = defaultdict(dict)
for package, version in c38.items():
    pins[package][38] = version
for package, version in c39.items():
    pins[package][39] = version
for package, version in c310.items():
    pins[package][310] = version
for package, version in c311.items():
    pins[package][311] = version
for package, version in c312.items():
    pins[package][312] = version

# Combine them.
combi = []
for package, versions in pins.items():
    py38_version = versions.pop(38, None)
    py39_version = versions.pop(39, None)
    py310_version = versions.pop(310, None)
    py311_version = versions.pop(311, None)
    py312_version = versions.pop(312, None)
    if py38_version == py39_version == py310_version == py311_version == py312_version:
        # All versions are the same.
        combi.append(f"{package}=={py311_version}")
        continue
    # Some versions are different or missing.
    # Start with the lowest Python.
    # Check if Python 3.8 differs from the rest.
    if py38_version is not None:
        combi.append(f'{package}=={py38_version}; python_version == "3.8"')

    # Check if Python 3.9 differs from the rest.
    if py39_version == py310_version == py311_version == py312_version and py39_version is not None:
        combi.append(f'{package}=={py39_version}; python_version >= "3.9"')
        continue
    if py39_version is not None:
        combi.append(f'{package}=={py39_version}; python_version == "3.9"')

    # Check if Python 3.10 differs from the rest.
    if py310_version == py311_version == py312_version and py310_version is not None:
        combi.append(f'{package}=={py310_version}; python_version >= "3.10"')
        continue
    if py310_version is not None:
        combi.append(f'{package}=={py310_version}; python_version == "3.10"')

    # Check if Python 3.11 differs from the rest.
    if py311_version == py312_version and py311_version is not None:
        combi.append(f'{package}=={py310_version}; python_version >= "3.11"')
        continue
    if py311_version is not None:
        combi.append(f'{package}=={py311_version}; python_version == "3.11"')

    # Check if Python 3.12 differs from the rest.
    if py312_version is not None:
        combi.append(f'{package}=={py312_version}; python_version >= "3.12"')

output = "\n".join(combi) + "\n"
# sanity check:
assert "==None" not in output
with open(constraints, "w") as myfile:
    myfile.write(output)
print(f"Wrote combined constraints for all Python versions to {constraints}.")
