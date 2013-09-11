# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os, sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# Add the directory which contains this file to PYTHONPATH temporarily.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def _readme():
    with open("README.rst") as f:
        return f.read()

setup(name='fuzzydict',
      version='0.0.1',
      description='FuzzyDict, an ambiguous dictionary',
      long_description=_readme(),
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          ],
      keywords='data structure dictionary fuzzy',
      author='Shoji Ihara',
      author_email='shoji.ihara@gmail.com',
      url='https://github.com/shoz/fuzzydict',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite="tests.test_fuzzydict",
      license='MIT')
