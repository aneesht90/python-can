#!/usr/bin/env python
# coding: utf-8

"""
python-can requires the setuptools package to be installed.
"""

import re
import logging
from setuptools import setup, find_packages

logging.basicConfig(level=logging.WARNING)

with open('can/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('README.rst', 'r') as f:
    long_description = f.read()

tests_require = [
    'mock',
    'nose',
    'pyserial >= 3.0',
    'subprocess32 >= 3.2',
]

setup(

    # Description
    name="python-can",
    url="https://github.com/hardbyte/python-can",
    description="Controller Area Network interface module for Python",
    long_description=long_description,

    # Code
    version=version,
    packages=find_packages(),
    
    # Author
    author="Brian Thorne",
    author_email="brian@thorne.link",

    # License
    license="LGPL v3",

    # Package data
    package_data={
        "": ["CONTRIBUTORS.txt", "LICENSE.txt"],
        "doc": ["*.*"]
    },

    # Installation
    install_requires=[
        'setuptools',
        #'Deprecated >= 1.1.0',
    ],
    extras_require={
        'serial': ['pyserial >= 3.0'],
        'neovi': ['python-ics'],
        'test': tests_require
    },

    # Testing
    test_suite="nose.collector",
    tests_require=tests_require,
)
