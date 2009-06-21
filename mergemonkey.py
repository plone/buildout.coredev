"""
This is a first cut at making svn merge tracking easier for a large scale
of branches to track.

TODO:

- Better argument handling, based on optparse or so.
- A more convinient merge command, that knows about the correct branch to
  take the revisions from.
- A "merge all missing" command to batch process all missing revisions
- Some form of status command that can tell if there's any missing merges,
  most useful in a similar form of "svn status" detailing the status for
  all tracked packages, even though this is properly slow.
- Turn this into a buildout recipe, so the previous and current source files
  can be tracked properly.
"""

import os
import subprocess
import sys
import urllib
import ConfigParser


HERE = os.path.abspath(os.curdir)
SRC = os.path.join(HERE, 'src')
PREVIOUS_SOURCES = 'http://svn.plone.org/svn/plone/buildouts/plone-coredev/branches/4.0/sources.cfg'
CURRENT_SOURCES = os.path.join(HERE, 'sources.cfg')

NEW_PACKAGE = 'Newly added package'
SAME_BRANCH = 'Previous version uses the same branch'


def extract_sources(sourcefile):
    config = ConfigParser.RawConfigParser()
    # We want to preserve case sensitivity
    config.optionxform = lambda s: s

    if sourcefile.startswith('http'):
        fd = None
        try:
            fd = urllib.urlopen(sourcefile)
            config.readfp(fd)
        finally:
            if fd is not None:
                fd.close()
    else:
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
    eligible_command = 'svn mergeinfo --show-revs eligible %(branch)s %(trunk)s'
    log_command = 'svn log --incremental -%(rev)s %(branch)s'
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
                p = subprocess.Popen(eligible_command % dict(
                    branch=branch, trunk=trunk),
                    cwd=HERE, shell=True, stdout=subprocess.PIPE,
                )
                p.wait()
                out = p.stdout.read()
                del p
                if '-v' in args or '--verbose' in args:
                    out = out.split('\n')
                    out = [o.strip() for o in out if o]
                    rev_string = ' -'.join(out)
                    os.system(log_command % dict(
                        rev=rev_string,
                        branch=branch,
                    ))
                    print('-' * 72)
                else:
                    print(out)
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
