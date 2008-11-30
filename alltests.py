"""
This script assumes to be called via python alltests.py while the current
directory is the buildout root.
"""

import os
import sys

disabled = [
    '.svn',
    'chameleon.core',
    'chameleon.zpt',
    'cmf.pt',
    'five.pt',
    'repoze.zope2',
    'sourcecodegen',
    'z3c.pt',
    'Products.ZopeVersionControl',
    'Zope2',
]

package_map = {
    'Plone' : 'Products.CMFPlone',
}

def main(args=[]):
    curdir = os.curdir
    test = os.path.join(curdir, 'bin', 'test')

    src = os.path.join(curdir, 'src')
    packages = []
    for directory in os.listdir(src):
        if directory not in disabled:
            setup = os.path.join(src, directory, 'setup.py')
            if os.path.exists(setup):
                name = package_map.get(directory, directory)
                packages.append(name)

    arg = ' '.join(args)

    errors = []
    for p in packages:
        print '#### Running tests for %s ####' % p
        value = os.system('%s -1 %s -s %s' % (test, arg, p))
        if value > 0:
            errors.append(p)
        print '#### Finished tests for %s ####' % p

    print
    print '#### Begin test results ####'
    for e in errors:
        print 'Failing tests in %s' % e
    print '#### End test results ####'

    if len(errors) > 0:
        return 1
    return 0

if __name__ == '__main__':
    args = sys.argv[1:]
    result = main(args)
    sys.exit(result)
