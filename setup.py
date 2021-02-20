#!/usr/bin/env python
from distutils.core import setup
name = 'newtron-radio'

setup(name=name,
      version='1.0',
      py_modules=['newtron-radio'],
      description='Internet Radio for Raspberrypi',
      url='https://github.com/msandres13/newtron-radio',
      author='Michael Andres',
      author_email='newtron-radio@andres.one',
      license='MIT',
      long_description="Long description of your tool",
      # data files in MANIFEST.in
      include_package_data=True,
      install_requires=[
          'python-mpd2',
          'pygame',
          'svg'
      ],
      entry_points={
          'console_scripts': ['newtron-radio = newtron-radio:main', ], },
      )
