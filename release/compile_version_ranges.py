"""Compile version ranges in buildout versions files.

This can be useful for release managers and others who want to update lots of versions.
The idea is to make a few temporary changes:

- in bare.cfg set allow-picked-versions = true
- in checkouts.cfg comment out all checkouts (and do 'bin/develop reset')
- in the various versions files, replace all or parts of the versions with ranges

Then:

- run buildout
- copy the list of picked versions and put them in the versions files,
  undoing the change to version ranges
- sort alphabetically case insensitively
- undo the other changes

Usage examples:

Allow bugfix releases in versions.cfg:

    bin/zopepy release/compile_version_ranges.py versions.cfg

Allow minor releases in versions-extra.cfg:

    bin/zopepy release/compile_version_ranges.py --minor versions-extra.cfg

Only set minimum versions, and do this in all versions files:

    bin/zopepy release/compile_version_ranges.py --minimum versions*.cfg

You can also copy only a part of versions.cfg to a new file, and run the script on that one.

By default the result is written on stdout.
To write back to the original file, use --write.
"""
from pathlib import Path

import sys

try:
    from packaging.version import parse, Version
except ImportError:
    from setuptools._vendor.packaging.version import parse, Version


# By default we only allow bugfix releases.
MINOR = "--minor" in sys.argv
MAJOR = "--major" in sys.argv
if MINOR and MAJOR:
    print("Only --minor or --major please.")
    sys.exit(1)

# By default we do not write, but only print to stdout.
WRITE = "--write" in sys.argv
paths = []
for arg in sys.argv[1:]:
    if arg.startswith("--"):
        continue
    paths.append(Path(arg))


def get_range(pin):
    """Get a version range for the package.

    By default we only allow bugfix releases.
    """
    package, version = pin.replace(" ", "").split("=")
    if not isinstance(parse(version), Version):
        # unrecognized: LegacyVersion
        return
    if MAJOR:
        # simply set a minimum version
        # pip: DateTime>=4.5
        # buildout: DateTime = >= 4.5
        return f"{package} = >={version}"
    version_parts = version.split(".")
    if MINOR:
        # pip: DateTime~=4
        # buildout: DateTime = >= 4.8, == 4.*
        star_version = f"{version_parts[0]}.*"
        minimum_version = ".".join(version_parts[:2])
        return f"{package} = >= {minimum_version}, == {star_version}"
    # bugfix only
    version = ".".join(version.split(".")[:3])
    if version.count(".") == 1:
        # 1.2 -> 1.2.0
        version += ".0"
    # pip: DateTime~=4.0.4
    # buildout: DateTime = >= 4.0.4, == 4.0.*
    star_version = ".".join(version_parts[:2] + ["*"])
    minimum_version = version
    return f"{package} = >= {minimum_version}, == {star_version}"


for path in paths:
    print(f"Handling {path}")
    with path.open() as myfile:
        lines = myfile.read().splitlines()
    new_lines = []
    for line in lines:
        if not line or line[0] in ("# [") or line.count("=") != 1:
            new_lines.append(line)
            continue
        new_line = get_range(line)
        # use the new line or the original
        new_lines.append(new_line or line)
    if WRITE:
        with path.open("w") as myfile:
            for line in new_lines:
                myfile.write(f"{line}\n")
    else:
        print("\n".join(new_lines))
