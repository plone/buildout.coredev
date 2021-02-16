# -*- coding: utf-8 -*-
"""Combine constraints2.txt and constraints3.txt into constraints.txt.

See tox.ini.
"""
import os
import sys

if not len(sys.argv) == 2:
    print("ERROR. Usage: create-constraints.py <directory with contraints files>")
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
constraints3 = os.path.join(directory, "constraints3.txt")
constraints2 = os.path.join(directory, "constraints2.txt")
for filename in (constraints2, constraints3):
    if not os.path.exists(filename):
        print(f"ERROR: {filename} does not exist.")
        print("Run: tox -p auto -e constraints2,constraints3,constraints")
        sys.exit(1)

# import pdb; pdb.set_trace()
c2 = parse_file(constraints2)
c3 = parse_file(constraints3)
combi = []
for package, py2_version in c2.items():
    py3_version = c3.pop(package, None)
    if py3_version:
        if py2_version == py3_version:
            # Python 2 and 3 have same version pin.
            combi.append(f"{package}=={py2_version}")
        else:
            # Python 2 and 3 have different version pin.  Add both.
            combi.append(f'{package}=={py2_version}; python_version < "3.0"')
            combi.append(f'{package}=={py3_version}; python_version >= "3.0"')
    else:
        # Python 2 only
        combi.append(f'{package}=={py2_version}; python_version < "3.0"')

# The rest in c3 is Python 3 only.
for package, py3_version in c3.items():
    combi.append(f'{package}=={py3_version}; python_version >= "3.0"')

with open(constraints, "w") as myfile:
    myfile.write("\n".join(combi) + "\n")
print(f"Wrote combined Python 2 and 3 constraints to {constraints}.")
