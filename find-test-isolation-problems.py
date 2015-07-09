# -*- coding: utf-8 -*-
import argparse
import ConfigParser
import subprocess


def probe_egg(package, test_egg):
    args = [
            'bin/test',
            '-s',
            package,
            '-s',
            test_egg,
        ]
    print('Probing {0}'.format(test_egg))
    try:
        subprocess.check_output(args)
    except subprocess.CalledProcessError as e:
        print('### FAILURE ###')
        print('{} has test isolation issues.'.format(test_egg))
        print('--')
        print(e.output)
        print('--')
        print('### FAILURE ###')
        print('')


def find_test_isolation_problems(package):
    """Read packages in the plone_app_testing alltests group from tests.cfg
       and probe them for test isolation issues.
    """
    tests_config = ConfigParser.ConfigParser()
    tests_config.readfp(open('tests.cfg'))
    test_eggs = tests_config.get("test-groups", "plone_app_testing")
    test_eggs = [
        x.split(' ')[0]
        for x in test_eggs.split('\n')
        if len(x) > 0 and '$' not in x and x != package
    ]
    for test_egg in test_eggs:
        probe_egg(package, test_egg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('package')
    args = parser.parse_args()

    find_test_isolation_problems(args.package)
