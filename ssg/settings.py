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


def init(root):
    '''Initialise settings from default values and config.py, in the a
    directory.

    :param root: Root directory of the site
    :type root: string
    '''
    global DEBUG

    if root is not None:
        SETTINGS['ROOTDIR'] = root

    try:
        # Import config.py
        config = SourceFileLoader('config', SETTINGS['ROOTDIR'] +
                                  '/config.py').load_module()
        # Update settings with values from config.py
        SETTINGS.update(config.CONFIG)
    except FileNotFoundError:
        logger.warning("No config.py found, using default values.")
    except SyntaxError as exception:
        logger.error('Syntax error in configuration file.')
        logger.error(str(exception.lineno) + ':' + str(exception.offset) +
                     ': ' + exception.text)
        exit(1)


def write_config(path):
    '''
    Write the value of the SETTINGS dictionary to ``config.py``.

    :param path: Path pointing to where the file should be written.
    :type path: string
    '''
    logger.debug("Writing configuration file.")
    # Open file
    with open(os.path.join(path, 'config.py'), 'w') as conf_file:
        # Write dictionary definition
        conf_file.write('CONFIG = {\n')
        # Run though all keys
        for name in SETTINGS.keys():
            # Write key name
            conf_file.write("'" + name + "': ")
            # Write value
            if isinstance(SETTINGS[name], str):
                conf_file.write("'")
            conf_file.write(str(SETTINGS[name]))
            if isinstance(SETTINGS[name], str):
                conf_file.write("'")
            conf_file.write(',\n')

        # Close the dictionary definition
        conf_file.write('}\n')
