#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup
from setuptools import find_packages

requirements = [
    'pandas',
    'bs4',
    'lxml',
    'numpy',
    'requests',
    'PyMySQL',
    'sqlalchemy',
]

setup_requirements = []


setup(
    name='api_wrappers',
    version='0.0.1',
    description='This package provides a wrapper around commercial apis',
    url='https://github.com/Mario8289/api_wrappers',
    author="Anthony Marriott",
    author_email='amarriott289@gmail.com',
    packages=find_packages(include=['api_wrappers', 'api_wrappers.*']),
    install_requires=requirements,
    zip_safe=False,
)