"""
This is a first cut at making svn merge tracking easier for a large scale
of branches to track.

TODO:

- Add a verbose option to --missing, so one can get a direct list of the
  svn log of all revisions that still should be merged. The revision number
  alone isn't very helpful.
- Better argument handling, based on optparse or so.
- A more convinient merge command, that knows about the correct branch to
  take the revisions from.
- A "merge all missing" command to batch process all missing revisions
- Some form of status command that can tell if there's any missing merges,
  most useful in a similar form of "svn status" detailing the status for
  all tracked packages, even though this is properly slow.
- Turn this into a buildout recipe, so the previous and current source files
  can be tracked properly and the previous one can come from an URL.
"""

import os
import sys
import ConfigParser


HERE = os.path.abspath(os.curdir)
SRC = os.path.join(HERE, 'src')
PREVIOUS_SOURCES = os.path.join(HERE, os.pardir, '40', 'sources.cfg')
CURRENT_SOURCES = os.path.join(HERE, 'sources.cfg')

NEW_PACKAGE = 'Newly added package'
SAME_BRANCH = 'Previous version uses the same branch'


def extract_sources(sourcefile):
    config = ConfigParser.RawConfigParser()
    # We want to preserve case sensitivity
    config.optionxform = lambda s: s
    config.read(sourcefile)

    raw_sources = dict(config.items('sources'))
    sources = {}
    # Strip out the svn prefix to the source line
    for k,v in raw_sources.items():
        sources[k] = v.split()[1]
    return sources


def prepare_sources():
    previous_sources = extract_sources(PREVIOUS_SOURCES)
    current_sources = extract_sources(CURRENT_SOURCES)

    sources = {}
    for k,v in current_sources.items():
        if k in previous_sources:
            previous = previous_sources[k]
            if previous == v:
                sources[k] = SAME_BRANCH
            else:
                sources[k] = dict(
                    current=v,
                    previous=previous,
                )
        else:
            sources[k] = NEW_PACKAGE
    return sources


def match_name(keys, name):
    matches = []
    for k in sorted(keys):
        if name not in k:
            continue
        if k not in matches:
            matches.append(k)
    return matches


def missing(args, sources):
    command = 'svn mergeinfo --show-revs eligible %(branch)s %(trunk)s'
    name = args[1]
    names = match_name(sources.keys(), name)
    if not names:
        print("No distribution with the name %s could be found." % name)
        return
    name = names[0]
    trunk = os.path.join(SRC, name)
    if os.path.exists(trunk):
        branchinfo = sources.get(name)
        if branchinfo is not None:
            if isinstance(branchinfo, dict):
                branch = branchinfo.get('previous')
                print("Determining missing merges for %s, based on %s" %
                      (name, branch))
                os.system(command % dict(
                    branch=branchinfo['previous'], trunk=trunk)
                )
            else:
                print("Couldn't compute merge info: %s" % branchinfo)
    else:
        print("Missing source directory: %s not found." % trunk)


def main(args):
    sources = prepare_sources()

    if len(args) > 1:
        if '--missing' in args:
            missing(args, sources)
    else:
        print("Not enough arguments.")


def help():
    print("This script currently only works on Hanno's laptop. "
          "It will be made more general soon (tm). ")
    print("---")
    print("Use this script via python mergemonkey.py --missing "
          "<distribution name> where <distribution name> is the name or a "
          "unique substring of the name of a distribution checked out in src."
         )
    print("---" + __doc__)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0 or '--help' in args:
        help()
    else:
        main(args)
