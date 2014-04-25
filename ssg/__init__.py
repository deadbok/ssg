import logging
import os
import markdown
from ssg.log import logger, init_file_log, init_console_log, close_log


__version__ = '0.0.1'


class ContentParserError(RuntimeError):
    '''
    The client has received an unexpected response
    '''
    pass


def get_content_files(path, extension):
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
                filelist.extend(get_content_files(filename, extension))
            else:
                _, ext = os.path.splitext(filename)
                if (ext == extension):
                    logger.debug("Found: " + filename)
                    filelist.append(filename)
    return(filelist)


def read_metadata(file):
    '''Read metadata from a content file.

    Throws a ContentParserError exception if no metadata is found.

    :param file: The file to read from.
    :type file: file
    :returns: The metadata.
    '''
    metadata = dict()

    line = file.readline()
    if not line.startswith('---'):
        raise ContentParserError('No metadata found.')
    # Run through lines until a line that starts with '...'
    line = file.readline()
    while not line.startswith('...'):
        meta = line.split(':')
        metadata[meta[0].strip()] = meta[1].strip()
        line = file.readline()
    return(metadata)



def init(debug=False):
    '''Initialise ssg

    :param debug: True enables debugging to console
    '''
    init_file_log(logging.DEBUG)
    if debug:
        init_console_log(logging.DEBUG)
    else:
        init_console_log(logging.INFO)


def process_content(path):
    '''Process all contents, converting it to HTML.

    :param path: Where the content files are at.
    :type path: string
    :returns: A list of tuples of metadata and content
    '''
    logger.info("Processing content.")
    contents = list()
    # Get list of files
    content_files = get_content_files(path, '.md')

    for filename in content_files:
        with open(filename, 'r') as markdown_file:
            logger.debug("Reading metadata from: " + filename)
            metadata = read_metadata(markdown_file)
            logger.debug("Reading markdown from: " + filename)
            md = markdown_file.read()
            content = markdown.markdown(md, output_format='html5')
            contents = (metadata, content)
    return(contents)


def close():
    '''
    Perform cleanup.
    '''
    close_log()
