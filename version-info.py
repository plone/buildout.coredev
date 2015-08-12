#!./bin/python
from argparse import ArgumentParser
from collections import OrderedDict
from ConfigParser import ConfigParser
from ConfigParser import NoOptionError
from ConfigParser import NoSectionError
import os.path
import urllib2


parser = ArgumentParser(
    description="Print info about pinned versions and its overrides"
)
parser.add_argument(
    "-b",
    "--buildout",
    help='path to buildout.cfg or other cfg file',
    default='buildout.cfg'
)

args = parser.parse_args()

version_sections = OrderedDict()


def extract_versions_section(filename):
    config = ConfigParser()
    if os.path.isfile(filename):
        config.read(filename)
    else:
        response = urllib2.urlopen(filename)
        config.readfp(response)
    # first read own versions section
    if config.has_section('versions'):
        version_sections[filename] = OrderedDict(config.items('versions'))
    try:
        extends = config.get('buildout', 'extends').strip()
    except (NoSectionError, NoOptionError):
        return
    for extend in extends.splitlines():
        if extend.strip():
            extract_versions_section(extend.strip())


extract_versions_section(args.buildout)

pkgs = {}
pkg_maxlen = 0
ver_maxlen = 0

for name in version_sections:
    for pkg in version_sections[name]:
        if pkg not in pkgs:
            pkgs[pkg] = OrderedDict()

for pkg in pkgs:
    pkg_maxlen = len(pkg) if len(pkg) > pkg_maxlen else pkg_maxlen
    for name in version_sections:
        if pkg in version_sections[name]:
            ver = version_sections[name][pkg]
            pkgs[pkg][name] = ver
            ver_maxlen = len(ver) if len(ver) > ver_maxlen else ver_maxlen

for pkg in sorted(pkgs):
    print pkg.ljust(pkg_maxlen, '.'),
    for idx, name in enumerate(pkgs[pkg]):
        version = pkgs[pkg][name].ljust(ver_maxlen, '.')
        if idx == 0:
            print version + ' ' + name
        else:
            print ' ' * (pkg_maxlen + 1) + version + ' ' + name
