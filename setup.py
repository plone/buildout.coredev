# -*- coding: utf-8 -*-
"""setuptools mock for tox."""

from setuptools import find_packages
from setuptools import setup


setup(
    name='buildout.coredev',
    version='1.0',
    description='Plone Core Development Buildout',
    long_description='',
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='Python Plone',
    author='Plone Foundation',
    author_email='',
    url='https://github.com/plone/buildout.coredev',
    license='GPL version 2',
    zip_safe=False,
    install_requires=[],
    extras_require={},
    entry_points="""""",
)
