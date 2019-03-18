#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    CBDict

    A tool to translate English to Chinese.

    date: 18/03/2019
    author: oliverxu
    homepage: https://blog.oliverxu.cn
    license: MIT
    copyright: Copyright (c) 2019 oliverxu. All rights reserved
"""

import codecs
import CBDict
import setuptools


# -*- Long Description -*-

def long_description():
    try:
        return codecs.open('README.md', 'r', 'utf-8').read()
    except IOError:
        return 'Long description error: Missing README.rst file'


setuptools.setup(
    name=CBDict.__name__,
    version=CBDict.__version__,
    description=CBDict.__description__,
    long_description=long_description(),
    keywords=CBDict.__keywords__,
    author=CBDict.__author__,
    author_email=CBDict.__contact__,
    url=CBDict.__url__,
    license=CBDict.__license__,
    platforms=['linux'],
    packages = setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Topic :: Terminals',
        "Topic :: System :: Distributed Computing",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        "requests",
        "pyperclip"
    ],
    entry_points={
        'console_scripts': [
            'CBDict = CBDict:main',
        ],
    },
)