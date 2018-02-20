#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from setuptools import setup

setup(
    name = 'fibonacci.py',
    version='1.0',
    license='GNU General Public License v3',
    author='Cindy Brown',
    author_email='ceeblet@gmail.com',
    description='Fibonacci restful web service',
    packages=['fibonacci'],
    platforms='any',
    install_requires=[
        'flask',
    ],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)