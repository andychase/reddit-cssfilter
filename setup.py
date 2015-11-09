#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def readme_or_docstring(): 
    path = os.path.join(os.path.dirname(__file__), 'readme.rst')
    if os.path.isfile(path):
        return open(path).read()
    else:
        import reddit_cssfilter.cssfilter
        return reddit_cssfilter.cssfilter.__doc__

setup(name='reddit-cssfilter',
      version='1.1',
      description='Parse and validate a safe subset of CSS',
      long_description=readme_or_docstring(),
      author='reddit',
      author_email='reddit@reddit.com',
      packages=['reddit_cssfilter'],
      package_data={'': ['LICENSE', 'readme.rst']},
      install_requires=[
        "tinycss2",
      ],
      url='https://github.com/andychase/reddit-css',
      download_url="https://github.com/andychase/reddit-css/archive/master.zip",
      license="CPAL"
      )
