'''
setup.py for setuptools.

Lifted from the PyPa github repository.
'''
from setuptools import setup, find_packages
import codecs
import os
import re


here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the relevant file
with codecs.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="Static Site Generator",
    version=find_version('ssg/__init__.py'),
    packages=find_packages(),
    scripts=['scripts/ssg'],

    install_requires=['jinja2', 'markdown'],

    author="Martin Grønholdt",
    author_email="martin.groenholdt@gmail.com",
    description="SSG is a program to generate static websites.",
    license="GPL",
    keywords="static web www ",
    url="http://github.com/deadbok/SSG",
)
