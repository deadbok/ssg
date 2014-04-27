'''
Assorted tools used in multiply places.

:since: 27/04/2014
:author: oblivion
'''
import os
from fnmatch import fnmatch
from ssg.log import logger


def get_files(path, extension):
    '''Get a list of files with extension from path an subdirectories.

    :param path: Path to look for files
    :type path: string
    :param extension: extension to look for
    :type extension: string
    '''
    filelist = list()

    logger.debug('Looking in "' + path + '" for files with extension "'
                 + extension + '"')
    for entry in os.listdir(path):
        # Ignore . and ..
        if not (entry.find('.') == 0):
            filename = path + "/" + entry
            # Process subdirectories
            if os.path.isdir(filename):
                filelist.extend(get_files(filename, extension))
            else:
                if fnmatch(filename, '*' + extension):
                    logger.debug("Found: " + filename)
                    filelist.append(filename)
    return(filelist)
