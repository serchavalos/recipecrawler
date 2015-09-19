#!/usr/bin/env python

from distutils.core import setup

setup(name='RecipeCrawler',
      version='0.1',
      description='Recipe Crawler',
      author='Sergio Avalos',
      autho_email='sergio.avalos@gmail.com',
      packages=['recipecrawler'],
      package_dir={'recipecrawler': 'src'}
    )