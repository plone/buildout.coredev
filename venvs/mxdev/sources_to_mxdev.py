"""Script to merge sources.cfg into mxdev.ini.

This was made for https://github.com/plone/buildout.coredev
around version 6.0.1.
Call this from the buildout directory.
You should have a mxdev.ini already.
If you want to use this for your own project, just copy the script and adapt.
"""
import configparser


mxdev = configparser.ConfigParser()
mxdev.read("mxdev.ini")
buildout = configparser.ConfigParser()
buildout.read("sources.cfg")
for (key, value) in buildout["remotes"].items():
    mxdev["settings"][key] = value

checkouts = configparser.ConfigParser()
checkouts.read("checkouts.cfg")
auto_checkouts = checkouts["buildout"]["auto-checkout"].lower().splitlines()
for (key, value) in buildout["sources"].items():
    # Something like:
    # ('docs', 'git ${remotes:plone}/documentation.git pushurl=${remotes:plone_push}/documentation.git egg=false branch=6-dev path=${buildout:docs-directory}')
    key = key.lower()
    if key not in mxdev.sections():
        mxdev.add_section(key)
    section = mxdev[key]
    values = value.split()
    if values[0] != "git":
        print(f"non-git ignored: {key} = {value}")
        continue
    section["url"] = values[1].replace("${remotes:", "${settings:")
    for part in values[2:]:
        # These should all be 'name=setting'.
        name, setting = part.split("=")
        if name == "pushurl":
            section[name] = setting.replace("${remotes:", "${settings:")
            continue
        if name == "branch":
            section[name] = setting
            continue
        if name == "egg":
            if setting.lower() == "false":
                section["install-mode"] = "skip"
            continue
        if name == "path":
            if setting == "${buildout:docs-directory}":
                setting = "documentation"
            section["target"] = setting
            continue
        print("WARNING: name '{name}' not recognized in line: {key} = {value}")
    if key in auto_checkouts:
        section["use"] = "true"

OUTFILE = "mxdev.out"
with open(OUTFILE, "w") as myfile:
    mxdev.write(myfile)
print(f"Output is in {OUTFILE}")
print("Comments from mxdev.ini are lost.")
print("You may want to copy only the remotes and sources to mxdev.ini.")
