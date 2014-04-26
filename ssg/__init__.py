'''
Main routines for the Static Site Generator.

:author: deadbok
'''

import logging
import os
import markdown
from jinja2 import Environment, FileSystemLoader
from ssg.log import logger, init_file_log, init_console_log, close_log
from ssg.metaext import parsers_run
from ssg import settings

__version__ = '0.0.1'

MARKDOWN_EXTENSIONS = ['extra', 'meta']
'''Markdown extension to use.'''


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


def init(debug=False):
    '''Initialise ssg

    :param debug: True enables debugging to console
    '''
    init_file_log(logging.DEBUG)
    if debug:
        init_console_log(logging.DEBUG)
    else:
        init_console_log(logging.INFO)
    settings.init()


def process_content(path):
    '''Process all contents, converting it to HTML.

    **Note: Metadata need to start at the first line of the file, and to have ONE
           newline before the content.**

    :param path: Where the content files are at.
    :type path: string
    :returns: A list of tuples of metadata and content
    '''
    logger.info("Processing content.")
    contents = list()
    # Get list of files
    content_files = get_content_files(path, '.md')

    # Run through the files
    for filename in content_files:
        # Open it
        with open(filename, 'r') as markdown_file:
            # Create a dictionary for metadata
            metadata = dict()
            logger.debug("Reading markdown from: " + filename)
            # Create an instance of the Markdown processor
            md = markdown.Markdown(extensions=MARKDOWN_EXTENSIONS,
                                   output_format='html5')
            # Convert file to html
            content = md.convert(markdown_file.read())
            # Check for metadata
            if len(md.Meta) == 0:
                raise ContentParserError('No metadata found.')
            # Add metadata from the metadata markdown extension
            metadata.update(md.Meta)
            # Run through extra meta data parsers.
            metadata.update(parsers_run(filename))
            # Add the content to the list
            contents.append((metadata, content))
    return(contents)


def apply_templates(path, contents):
    '''Apply jinja2 templates to content, and write the files.

    :param path: Path to templates
    :type path: string
    :param contents: A list of metadata, content tuples
    :type contents: list
    '''
    logger.debug("Applying templates.")
    env = Environment(loader=FileSystemLoader(path))
    # Run through all content
    for metadata, content in contents:
        if 'template' in metadata.keys():
            template = metadata['template']
        else:
            logger.warning('Using index.html as template.')
            template = 'index.html'
        tpl = env.get_template(template)
        context = dict()
        context['metadata'] = metadata
        context['content'] = content
        result = tpl.render(context)
        # print(result)


def close():
    '''
    Perform cleanup.
    '''
    close_log()
