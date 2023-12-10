# -*- coding: utf-8 -*-
"""Parse sources from a buildout configuration and write to a mxdev compatible
ini file.

This script is called by 'tox -c release/tox.ini -e create-mxsources.py'

Manual usage: bin/python create-mxsources.py
"""

# From: create-constraints.py

import os
import sys

from zc.buildout import buildout

if not len(sys.argv) == 3:
    print("ERROR. Usage: create-mxsources.py buildout.cfg sources.ini")
    sys.exit(1)
config_file = sys.argv[1]
config_file = os.path.realpath(config_file)
sources_file = sys.argv[2]
sources_file = os.path.realpath(os.path.join(os.getcwd(), sources_file))
config = buildout.Buildout(config_file, [])

sources = config.get("sources", {})
remotes = config.get("remotes", {})

# Special case:
# Remove github and github_push from remotes in favor of zope and zope_push.
if "github" in remotes:
    del remotes["github"]
if "github_push" in remotes:
    del remotes["github_push"]

with open(sources_file, "w") as cfile:
    cfile.write(f"# File created by {os.path.relpath(__file__)}\n")
    cfile.write(f"# Parsed from {os.path.relpath(config_file)}\n")

    # Write the remotes.
    cfile.write("\n[settings]\n")
    cfile.write("\n# Remote definitions for source checkouts.\n")

    for key, val in sorted(remotes.items(), key=lambda x: x[0].lower()):
        cfile.write(f"{key} = {val}\n")

    # Write the sources
    cfile.write("\n")
    for key, val in sorted(sources.items(), key=lambda x: x[0].lower()):
        vals = val.split(" ")
        cfg = {}
        cfg[key] = {}
        for it in vals:
            it_ = it.split("=")
            if len(it_) == 1:
                if it_[0] == "git":
                    continue
                url = it_[0]
                # Replace the urls with remote definitions, if possible.
                for key_, val_ in remotes.items():
                    if url.startswith(val_):
                        url = url.replace(val_, f"${{settings:{key_}}}")
                        break
                cfg[key]["url"] = url
                continue

            if it_[0] == "pushurl":
                # Replace the urls with remote definitions, if possible.
                for key_, val_ in remotes.items():
                    if it_[1].startswith(val_):
                        it_[1] = it_[1].replace(val_, f"${{settings:{key_}}}")
                        break
                cfg[key]["pushurl"] = it_[0]

            if it_[0] == "egg":
                if it_[1].lower() == "true":
                    continue
                # We want to skip if egg is set to false.
                cfg[key]["install-mode"] = "skip"
                continue
            if it_[0] == "path":
                cfg[key]["target"] = os.path.relpath(it_[1])
                continue
            cfg[key][it_[0]] = it_[1]

        # Explicitly set the branch.
        # Default branch in buildout is "master", for git it is "main".
        if not cfg[key].get("branch"):
            cfg[key]["branch"] = "master"

        for name, cfg in cfg.items():
            cfile.write(f"\n[{name}]\n")
            for key_, val_ in sorted(cfg.items()):
                cfile.write(f"{key_} = {val_}\n")

print(f"Wrote all sources to {os.path.relpath(sources_file)}")
