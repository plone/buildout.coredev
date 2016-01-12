#!./bin/python
from argparse import ArgumentParser
from collections import OrderedDict
from ConfigParser import ConfigParser
from ConfigParser import NoOptionError
from ConfigParser import NoSectionError
import os.path
import urllib2
import urlparse

parser = ArgumentParser(
    description="Print info about pinned versions and its overrides"
)
parser.add_argument(
    "-b",
    "--buildout",
    help='path to buildout.cfg or other cfg file',
    default='buildout.cfg'
)
parser.add_argument(
    "-o",
    "--overrides",
    help='print only packages with overrides',
    action="store_true"
)

args = parser.parse_args()

version_sections = OrderedDict()


def extract_versions_section(filename, relative=None):
    if (
        relative is not None and
        "://" not in filename and
        not filename.startswith('/')
    ):
        filename = relative + '/' + filename
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
        extend = extend.strip()
        if not extend:
            continue
        sub_relative = relative
        if "://" in extend:
            parts = list(urlparse.urlparse(extend))
            parts[2] = '/'.join(parts[2].split('/')[:-1])
            sub_relative = urlparse.urlunparse(parts)
        elif '/' in extend:
            sub_relative = os.path.dirname(extend)
        extract_versions_section(extend, sub_relative)


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
    if args.overrides and len(pkgs[pkg]) < 2:
        continue
    print pkg.ljust(pkg_maxlen, '.'),
    for idx, name in enumerate(pkgs[pkg]):
        version = pkgs[pkg][name].ljust(ver_maxlen, '.')
        if idx == 0:
            print version + ' ' + name
        else:
            print ' ' * (pkg_maxlen + 1) + version + ' ' + name
