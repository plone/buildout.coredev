"""Initialize version constraints for Plone.

Call this in a virtualenv so packages get installed there.
So prerequisite is something like this:

    python3.11 -mvenv .
    bin/pip install -U pip setuptools wheel

The main goal is not actually to install the packages, this is just a happy side effect.
The main goal is to generate a few constraints files and version files.

Command line arguments for the script itself:

--help
-h
    Print this doc string.

We simply pass all other arguments to pip.
You will usually want to pass either a Zope constraints file or a previous Plone constraints file.

Examples:

--pre -c https://dist.plone.org/release/6.0-dev/constraints.txt
-c https://zopefoundation.github.io/Zope/releases/5.8/constraints.txt
-r https://dist.plone.org/release/6.0-dev/constraints.txt

The next option will be *very* useful when you want to check for new versions:

--upgrade-strategy eager

"""
import subprocess
import sys
import urllib.request

# For some packages, major releases are fine.
# This will be true for most calender based releases.
ALLOW_MAJOR = [
    "certifi",
    "pytz",
    "trove-classifiers",
]


def parse_options():
    # We do not need fancy argument parsing at the moment.
    options = sys.argv[1:]
    if "--help" in options or "-h" in options:
        print(__doc__)
        sys.exit(0)
    return options


def download_upstream_constraints():
    """Download the constraints files that are passed on the command line.

    Returns a tuple:
    - upstream constraint file names / paths
    - list of all constraints

    It could be nice to support paths as well, but currently we don't.
    """
    constraint = None
    upstream_constraints_files = []
    upstream_constraints = []
    # Maybe I should use argparse anyway...
    for opt in options:
        if opt == "-c":
            constraint = True
            continue
        if not constraint:
            continue
        upstream_constraints_files.append(opt)
        print(f"Downloading constraints file {opt}")
        req = urllib.request.Request(opt)
        with urllib.request.urlopen(req) as response:
            print(response.info())
            contents = response.read()
            for line in contents.decode("utf-8").splitlines():
                upstream_constraints.append(line)
        constraint = False
    return upstream_constraints_files, upstream_constraints


def run(command, **kwargs):
    print("Running command:")
    print(" ".join(command))
    return subprocess.run(command, check=True, **kwargs)


def get_range(pin, minor=False, minimum=False):
    """Get a version range for the package.

    By default we only allow bugfix releases.
    """
    package, version = pin.split("==")
    if PRE:
        # With '--pre' it makes sense to only set minimum versions.
        minimum = True
    if minimum or package in ALLOW_MAJOR:
        return f"{package}>={version}"
    version_parts = version.split(".")
    if minor:
        # 1.2.3 -> 1.2
        version = ".".join(version_parts[:2])
        return f"{package}~={version}"
    # bugfix only
    # 1.2.3.4 -> 1.2.3
    version = ".".join(version.split(".")[:3])
    if version.count(".") == 1:
        # 1.2 -> 1.2.0
        version += ".0"
    return f"{package}~={version}"


def freeze_constraints():
    """Freeze, but exclude a few items.

    Note that pip/setuptools/wheel are excluded by pip unless we call it with --all.
    We are happy to follow pip's lead here.

    We return the list of constraints.
    """
    process = run(
        ["bin/pip", "freeze", "--exclude-editable", "--exclude", "plonecoredev"],
        capture_output=True,
        text=True,
    )
    constraints_file = "constraints.txt"
    print(f"Writing {constraints_file}")
    with open(constraints_file, "w") as myfile:
        myfile.write(process.stdout)

    return process.stdout.splitlines()


def check_nothing_installed():
    process = run(
        ["bin/pip", "freeze", "--exclude-editable", "--exclude", "plonecoredev"],
        capture_output=True,
        text=True,
    )
    if process.stdout:
        print("This is not a clean virtualenv: packages are already installed.")
        print("Please remove the virtualenv files and then recreate it:")
        print("python3.11 -mvenv . && bin/pip install pip setuptools wheel")
        sys.exit(1)


# HERE WE REALLY START DOING STUFF.

# Parse the options.
options = parse_options()
PRE = "--pre" in options

# This should be a fresh virtualenv.
check_nothing_installed()

# Download the constraints files that are passed on the command line.
# Then we can see which packages we install that are not yet pinned upstream.
upstream_constraints_files, upstream_constraints = download_upstream_constraints()

# Install the core (Plone).
run(["bin/pip", "install", "-U", ".[core]"] + options)

# Freeze the constraints.
constraints = freeze_constraints()

# Add to the version ranges, allowing only bug fixes.
ranges = []
for pin in constraints:
    if pin not in upstream_constraints:
        upstream_constraints.append(pin)
        # Get version range allowing only bugfix releases.
        ranges.append(get_range(pin))


# Install all additional dependencies.
# Use the constraints file that we have just created.
run(
    ["bin/pip", "install", "-U", ".[buildout]", ".[ecosystem]", ".[test]", ".[tools]"]
    + options
    + ["-c", "constraints.txt"]
)

# Freeze the constraints again.
# This overwrites our previously generated constraints file.
constraints = freeze_constraints()

# Add to the version ranges, allowing minor/feature releases
for pin in constraints:
    if pin not in upstream_constraints:
        ranges.append(get_range(pin, minor=True))

# Write the ranges file.
ranges_file = "ranges.txt"
print(f"Writing {ranges_file}")
with open(ranges_file, "w") as myfile:
    for upstream in upstream_constraints_files:
        myfile.write(f"-c {upstream}\n")
    for dep in ranges:
        myfile.write(f"{dep}\n")

# Write the buildout versions file.
buildout_file = "versions.cfg"
print(f"Writing {buildout_file}")
with open(buildout_file, "w") as myfile:
    myfile.write("[versions]\n")
    for pin in constraints:
        pin = pin.replace("==", " = ")
        myfile.write(f"{pin}\n")

print("Done.")
