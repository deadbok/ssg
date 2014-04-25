'''

@since 23/04/2014
@author: oblivion
'''
import os
from ssg.log import logger
from importlib.machinery import SourceFileLoader


DEFAULT_CONFIG = {
    'SITENAME': 'Spam',
    'SITEURL': 'localhost',
    'ROOTDIR': os.getcwd(),
    'CONTENTDIR': 'content'
}
'''Default configuration values.'''

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

