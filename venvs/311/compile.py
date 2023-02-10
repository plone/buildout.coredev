"""Print constraints that are installed, but not pinned in Zope.

Prerequisites:

python3.11 -mvenv .
bin/pip install -U pip setuptools wheel -c https://dist.plone.org/release/6.0.1/constraints.txt
bin/pip install Plone -c https://dist.plone.org/release/6.0.1/constraints.txt
bin/pip freeze --exclude-editable > installed.txt
curl -o zope.txt https://zopefoundation.github.io/Zope/releases/5.8/constraints.txt

Usage:

bin/python compile.py | pbcopy

Edit pyproject.toml and paste the output into project.dependencies.
TODO: use tomli to directly write it.
"""
with open("installed.txt") as myfile:
    installed = myfile.read().splitlines()
with open("zope.txt") as myfile:
    zope = myfile.read().splitlines()
dependencies = []
for package in installed:
    if package not in zope:
        compatible = package.replace("==", "~=")
        dependencies.append(compatible)
        print(f'    "{compatible}",')
