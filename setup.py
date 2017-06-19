# -*- coding: utf-8 -*-
"""
behave-selenium
"""
from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()

VERSION = '0.0.5'

setup(name='behave-selenium',
      version=VERSION,
      description="High level behave steps to control Selenium",
      long_description=README,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Testing'
      ],
      keywords='bdd testing behave command line',
      author='Roberto Abdelkader Martínez Pérez',
      author_email='robertomartinezp@gmail.com',
      url='https://github.com/buguroo/behave-selenium',
      license='LGPLv3',
      packages=["behave_selenium",
                "behave_selenium.steps",
                "behave_selenium.steps.stepcollection",
                "behave_selenium.steps.naturalsearch"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ])
