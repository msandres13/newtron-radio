#!/usr/bin/env python
from setuptools import setup
import os

name = 'newtron-radio'


CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

LICENSE = """\The MIT License (MIT)

Copyright (c) 2014 5Volt-Junkie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

setup(name=name,
      version=1.0,
      py_modules=['newtron-radio'],
      description='Internet Radio for Raspberrypi',
      url='https://github.com/msandres13/newtron-radio',
      author='Michael Andres',
      author_email='newtron-radio@andres.one',
      python_requires='>=3.6',
      long_description=open('README.txt').read(),
      classifiers=CLASSIFIERS,
      license=LICENSE,
      # data files in MANIFEST.in
      include_package_data=True,
      install_requires=[
          'python-mpd2',
          'pygame',
          'svg'
      ]
#       entry_points="""
# # -*- Entry points: -*-
# """
#       entry_points={
#           'console_scripts': ['newtron-radio = newtron-radio:main', ], },
      )
