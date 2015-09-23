#!/usr/bin/env python

from setuptools import setup, find_packages

# TODO: Add dependencies: request, beautifulsoap4
setup(name='RecipeCrawler',
      version='0.1',
      description='Recipe Crawler',
      author='Sergio Avalos',
      author_email='sergio.avalos@gmail.com',
      packages=find_packages(),
#      install_requires=['beautifulsoap4'],
      test_suite='test',
    )