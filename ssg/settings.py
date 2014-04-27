'''
Configuration
=============

Configuration is done by adding values to the CONFIG dictionary found in the
file:`config.py` in the root of the site directory.

Default configuration values
----------------------------

SITENAME
    Name of the site. Default *Spam*

SITEURL
    URL of the site. Default *http://localhost/*

ROOTDIR
    Root directory of the ssg files. Default *current working directory*

CONTENTDIR
    Sub directory of ROOTDIR with site content. Default *content*

OUTPUTDIR
    Sub directory of ROOTDIR where the final site is saved. Default *output*

METAEXTS
    List of enabled meta data parsers. Default *empty*
'''
import os
from ssg.log import logger
from importlib.machinery import SourceFileLoader


DEFAULT_CONFIG = {
    'SITENAME': 'Spam',
    'SITEURL': 'http://localhost/',
    'ROOTDIR': os.getcwd(),
    'CONTENTDIR': 'content',
    'OUTPUTDIR': 'output',
    'METAEXTS': list()
}


SETTINGS = DEFAULT_CONFIG
'''Dictionary for all configuration values.'''


def init():
    '''
    Initialise settings from default values and config.py, in the current dir.
    '''
    try:
        # Import config.py
        config = SourceFileLoader('config', os.getcwd() +
                                  '/config.py').load_module()
        # Update settings with values from config.py
        SETTINGS.update(config.CONFIG)
    except FileNotFoundError as exception:
        logger.warning("No config.py found, using default values.")

