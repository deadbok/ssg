'''
Assorted tools used in multiply places.

:since: 27/04/2014
:author: oblivion
'''
import os
from fnmatch import fnmatch
from datetime import datetime
from ssg.log import logger
from ssg.settings import SETTINGS


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


def get_datetime(datetime_str):
    '''Get datetime object from a date, time string, formatted according to the
    DATEFORMAT configuration variable.

    :param datatime_str: String containing date and time.
    :type datatime_str: string
    '''
    logger.debug('Generating datetime object from: ' + datetime_str)
    ret = datetime.strptime(datetime_str, SETTINGS['DATEFORMAT'])
    logger.debug('datetime object: ' + str(ret))
    return(ret)