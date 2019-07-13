#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of tilda_wrapper_api.
# https://github.com/ozeranskiy/tilda_wrapper_api

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2019, Sergey Ozeranskiy <sergey.ozeranskiy@gmail.com>

# Standard libraries
import io

# Third party libraries
from setuptools import find_packages, setup

# Project
from tilda_wrapper_api import __author__, __version__

requires = [
    'requests',
    'dataclasses-json',
]

tests_require = [
    'isort',
    'mock',
    'nose',
    'requests_mock',
    'coverage',
    'tox',
    'sphinx',
    'sphinx_rtd_theme',
    'bump2version',
    'python-coveralls',
]

with io.open('README.md', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='tilda_wrapper_api',
    version=__version__,
    description='A python implementation of the Tilda API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='tilda api',
    author='Sergey Ozeranskiy',
    author_email=__author__,
    url='https://github.com/ozeranskiy/tilda_wrapper_api',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=requires,
    tests_require=tests_require,
    extras_require={},
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'tilda_wrapper_api=tilda_wrapper_api.cli:main',
        ],
    },
)
