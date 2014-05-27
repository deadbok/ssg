'''
Configuration is done by adding values to the CONFIG dictionary found in the
``config.py`` in the root of the site directory.

Default configuration values
----------------------------

AUTHOR
    Author of the site. Default *Eggs*

SITENAME
    Name of the site. Default *Spam*.

SITEURL
    URL of the site. Default *http://localhost/*.

ROOTDIR
    Root directory of the ssg files. Default *current working directory*.

CONTENTDIR
    Sub directory of ROOTDIR with site content. Default *content*.

TEMPLATEDIR
    Sub directory of ROOTDIR with site templates. Default *templates*.

OUTPUTDIR
    Sub directory of ROOTDIR where the final site is saved. Default *output*.

DATEFORMAT
    Format string to read the date in the content files. Default
    *%Y-%m-%d %H:%M*.
    :ref:`Format string directives <python:strftime-strptime-behavior>`

COPYSOURCES
    Copy source *.md files to output dirtectory. Default *True*

METAPARSERS
    List of enabled meta data parsers. Default *empty*.

GENERATORS
    List of enabled generators. Default *empty*.

CONTENTFILTERS
    List of enabled content filters. Default *empty*.
'''
from importlib.machinery import SourceFileLoader
import os

from ssg.log import logger


DEFAULT_CONFIG = {
    'AUTHOR': 'Eggs',
    'SITENAME': 'Spam',
    'SITEURL': 'http://localhost/',
    'ROOTDIR': os.getcwd(),
    'CONTENTDIR': 'content',
    'TEMPLATEDIR': 'templates',
    'OUTPUTDIR': 'output',
    'DATEFORMAT': '%Y-%m-%d %H:%M',
    'COPYSOURCES': True,
    'METAPARSERS': list(),
    'GENERATORS': list(),
    'CONTENTFILTERS': list()
}

# Dictionary for all configuration values.
SETTINGS = DEFAULT_CONFIG


def init():
    '''
    Initialise settings from default values and config.py, in the current dir.
    '''
    try:
        # Import config.py
        config = SourceFileLoader('config', SETTINGS['ROOTDIR'] +
                                  '/config.py').load_module()
        # Update settings with values from config.py
        SETTINGS.update(config.CONFIG)
    except FileNotFoundError:
        logger.warning("No config.py found, using default values.")
