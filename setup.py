"""
A Python3 program that searches a single MARC record via a given id (controlfield 001) in a given (binary) MARC records file and writes it into a single (binary) MARC file.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='searchmarcrecord',
      version='0.0.1',
      description='a Python3 program that searches a single MARC record via a given id (controlfield 001) in a given (binary) MARC records file and writes it into a single (binary) MARC file',
      url='https://github.com/slub/searchmarcrecord',
      author='Bo Ferri',
      author_email='zazi@smiy.org',
      license="Apache 2.0",
      packages=[
          'searchmarcrecord',
      ],
      package_dir={'searchmarcrecord': 'searchmarcrecord'},
      install_requires=[
          'argparse>=1.4.0',
          'pymarc>=3.1.7'
      ],
      entry_points={
          "console_scripts": ["searchmarcrecord=searchmarcrecord.searchmarcrecord:run"]
      }
      )
