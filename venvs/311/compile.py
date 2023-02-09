# Print constraints that are installed, but not pinned in Zope.
# Prerequisites:
# ./bootstrap.sh
# bin/pip freeze > installed.txt
# curl -o zope.txt https://zopefoundation.github.io/Zope/releases/5.8/constraints.txt
with open("installed.txt") as myfile:
    installed = myfile.read().splitlines()
with open("zope.txt") as myfile:
    zope = myfile.read().splitlines()
for package in installed:
    if package not in zope:
        print(package)
