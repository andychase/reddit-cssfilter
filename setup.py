#!/usr/bin/env python
"""
reddit-cssfilter
================

|Build Status|

cssfilter.py extracted from reddit's source code.

This library allows you to filter "unsafe" css from your users.

**This library requires attribution!:**

When using this library, reddit requires you to put the following information in the splash or the "about" section of your application.

  EXHIBIT B. Attribution Information

  Attribution Copyright Notice: Copyright (c) 2006-2015 reddit Inc. All Rights
  Reserved.

  Attribution Phrase (not exceeding 10 words): Powered by reddit

  Attribution URL: http://code.reddit.com

  Graphic Image as provided in the Covered Code:
  http://code.reddit.com/reddit_logo.png

Info
~~~~

Parse and validate a safe subset of CSS.

The goal of this validation is not to ensure functionally correct stylesheets
but rather that the stylesheet is safe to show to downstream users.  This
includes:

* not generating requests to third party hosts (information leak)
* xss via strange syntax in buggy browsers

Beyond that, every effort is made to allow the full gamut of modern CSS.


How to use
~~~~~~~~~~

.. code-block:: python

  import reddit_cssfilter.cssfilter
  cssfilter.validate_css(stylesheet, images)

..

  Validate and re-serialize the user submitted stylesheet.
  
  images is a mapping of subreddit image names to their URLs.  The
  re-serialized stylesheet will have %%name%% tokens replaced with their
  appropriate URLs.
  
  The return value is a two-tuple of the re-serialized (and minified)
  stylesheet and a list of errors.  If the list is empty, the stylesheet is
  valid.


Licence
~~~~~~~

Copyright (c) 2006-2015 reddit Inc. All Rights Reserved.

Common Public Attribution License Version 1.0 (CPAL)

The full license is available here: `reddit Inc. Common Public Attribution License Version 1.0 (CPAL) <http://code.reddit.com/LICENSE>`_.

.. |Build Status| image:: https://travis-ci.org/andychase/reddit-cssfilter.svg?branch=master
   :target: https://travis-ci.org/andychase/reddit-cssfilter

"""
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='reddit-cssfilter',
      version='1.2',
      description='Parse and validate a safe subset of CSS',
      long_description=__doc__,
      author='reddit',
      author_email='reddit@reddit.com',
      packages=['reddit_cssfilter'],
      package_data={'': ['LICENSE', 'readme.rst']},
      install_requires=[
        "tinycss2",
      ],
      classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
      url='https://github.com/andychase/reddit-cssfilter',
      download_url="https://github.com/andychase/reddit-cssfilter/archive/master.zip",
      license="Common Public Attribution License Version 1.0 (CPAL)"
      )
