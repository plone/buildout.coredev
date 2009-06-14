"""
This script assumes to be called via python alltests.py while the current
directory is the buildout root.
"""

import os
import sys

disabled = [
    '.svn',
    'borg.localrole',
    'repoze.zope2',
    'Products.ExtendedPathIndex',
    'Products.PasswordResetTool',
    'Products.PloneLanguageTool',
    'Products.PluggableAuthService',
    'Products.ResourceRegistries',
    'Products.ZopeVersionControl',
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
                try:
                    __import__(name)
                except ImportError:
                    pass
                else:
                    packages.append(name)

    arg = ' '.join(args)

    errors = []
    for p in sorted(packages):
        print '#### Running tests for %s ####' % p
        value = os.system('%s -1 --auto-progress --auto-color --exit-with-status %s -s %s' % (test, arg, p))
        if value > 0:
            errors.append(p)
        print '#### Finished tests for %s ####' % p
        print

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
