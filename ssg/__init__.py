import logging
import os
from log import logger, init_file_log, init_console_log


__version__ = '0.0.1'


def get_content_files(path, extension):
    """Get a list of files with extension from path an subdirectories."""
    filelist = list()

    logger.debug('Looking in "' + path + '" for files with extension "'
                 + extension + '"')
    for entry in os.listdir(path):
        # Ignore . and ..
        if not (entry.find('.') == 0):
            filename = path + "/" + entry
            # Process subdirectories
            if os.path.isdir(filename):
                filelist.append(get_content_files(filename, extension))
            else:
                if (os.path.splitext(filename) == extension):
                    logger.debug("Found: " + filename)
                    filelist.append(filename)


def init(debug=False):
    init_file_log(logging.DEBUG)
    if debug:
        init_console_log(logging.DEBUG)
    else:
        init_console_log(logging.INFO)
