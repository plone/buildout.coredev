"""
This is a first cut at making svn merge tracking easier for a large scale
of branches to track.

TODO:

- Better argument handling, based on optparse or so.
- Better help messages for the various commands. Look at mr.developer.
- Turn this into a buildout recipe, so the previous and current source files
  can be tracked properly.
"""

import os
import subprocess
import sys
import urllib
import ConfigParser


NEW_PACKAGE = 'Newly added package'
SAME_BRANCH = 'Previous version uses the same branch'

ELIGIBLE_COMMAND = 'svn mergeinfo --show-revs eligible %(branch)s %(trunk)s'
LOG_COMMAND = 'svn log --incremental -%(rev)s %(branch)s'
MERGE_COMMAND = 'svn merge -%(rev)s %(branch)s %(trunk)s'


def extract_sources(location):
    config = ConfigParser.RawConfigParser()
    # We want to preserve case sensitivity
    config.optionxform = lambda s: s

    if location.startswith('http'):
        fd = None
        try:
            fd = urllib.urlopen(location)
            config.readfp(fd)
        finally:
            if fd is not None:
                fd.close()
    else:
        config.read(location)

    raw_sources = dict(config.items('sources'))
    sources = {}
    # Strip out the svn prefix to the source line
    for k,v in raw_sources.items():
        sources[k] = v.split()[1]
    return sources


def prepare_sources(previous_location, current_location):
    previous_sources = extract_sources(previous_location)
    current_sources = extract_sources(current_location)

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


def get_locations(name, sources, quiet=False, src_dir=None):
    names = match_name(sources.keys(), name)
    if not names:
        if not quiet:
            print("No distribution with the name %s could be found." % name)
        return None
    else:
        name = names[0]
    if src_dir is None:
        src_dir = os.path.join(os.path.abspath(os.curdir), 'src')
    trunk = os.path.join(src_dir, name)
    if os.path.exists(trunk):
        branchinfo = sources.get(name)
        if branchinfo is not None:
            if isinstance(branchinfo, dict):
                return trunk, branchinfo.get('previous')
            else:
                if not quiet:
                    print("Couldn't compute merge info: %s" % branchinfo)
    else:
        if not quiet:
            print("Missing source directory: %s not found." % trunk)
    return None


def determine_missing(trunk, branch):
    p = subprocess.Popen(
        ELIGIBLE_COMMAND % dict(branch=branch, trunk=trunk),
        shell=True, stdout=subprocess.PIPE,
    )
    p.wait()
    out = p.stdout.read()
    del p
    out = out.split('\n')
    out = [o.strip() for o in out if o]
    return out


def missing(name, trunk, branch, quiet=False):
    print("Determining missing merges for %s, based on %s" % (name, branch))
    out = determine_missing(trunk, branch)
    if quiet:
        print('\n'.join(out))
    else:
        rev_string = ' -'.join(out)
        os.system(LOG_COMMAND % dict(rev=rev_string, branch=branch))
        print('-' * 72)


def mergeall(name, trunk, branch):
    print("Merging all missing revisions for %s, based on %s" % (name, branch))
    out = determine_missing(trunk, branch)
    print('Revisions to be merged: %s\n' % ', '.join(out))
    for rev in out:
        cs = rev.replace('r', 'c')
        command = MERGE_COMMAND % dict(rev=cs, branch=branch, trunk=trunk)
        os.system(LOG_COMMAND % dict(rev=cs, branch=branch))
        os.system(command)

def merge(name, trunk, branch, rev):
    print("Merging revisions %s for %s, based on %s" % (rev, name, branch))
    cs = rev
    if ':' not in rev:
        cs = rev.replace('r', 'c')
    command = MERGE_COMMAND % dict(rev=cs, branch=branch, trunk=trunk)
    os.system(LOG_COMMAND % dict(rev=cs, branch=branch))
    os.system(command)

def status(sources, repos=None):
    names = sorted(sources.keys())
    for name in names:
        info = get_locations(name, sources, quiet=True)
        if info is not None:
            trunk, branch = info
        else:
            continue
        if repos is not None:
            found = False
            for r in repos:
                if r in branch:
                    found = True
            if not found:
                continue
        result = determine_missing(trunk, branch)
        if len(result) > 0:
            print('M ' +  name + ' - missing revisions: %s' % len(result))
        else:
            print('  ' + name)


def main(args,
    previous_sources='http://svn.plone.org/svn/plone/buildouts/plone-coredev/branches/4.0/sources.cfg',
    current_sources=os.path.join(os.path.abspath(os.curdir), 'sources.cfg'),
    repos=['svn.plone.org'],
    ):
    sources = prepare_sources(previous_sources, current_sources)

    if len(args) > 1:
        name = args[1]
        info = get_locations(name, sources)
        if info is not None:
            trunk, branch = info
            if 'missing' in args or 'mi' in args:
                quiet = False
                if '-q' in args or '--quiet' in args:
                    quiet = True
                missing(name, trunk, branch, quiet=quiet)
            elif 'mergeall' in args or 'ma' in args:
                mergeall(name, trunk, branch)
            elif 'merge' in args or 'me' in args:
                if len(args) > 2:
                    rev = args[2]
                    merge(name, trunk, branch, rev)
    elif 'status' in args or 'st' in args:
        status(sources, repos=repos)
    else:
        print("Not enough arguments.")


def help():
    print("Use this script via python mergemonkey.py missing "
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
