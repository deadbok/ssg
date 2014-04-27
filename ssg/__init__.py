'''
Main routines for the Static Site Generator.

:author: deadbok
'''

import logging
import os
import markdown
from ssg import writer
from jinja2 import Environment, FileSystemLoader
from ssg.log import logger, init_file_log, init_console_log, close_log
from ssg.metaext import parsers_run
from ssg import settings
from ssg.settings import SETTINGS
from ssg.tools import get_files

__version__ = '0.0.1'

MARKDOWN_EXTENSIONS = ['extra', 'meta']
'''Markdown extension to use.'''


class ContentParserError(RuntimeError):
    '''
    The client has received an unexpected response
    '''
    pass


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

'''
Context
=======

A context is created for each processed file in the content directory. The
context contains all data about an output file.

Keys in the context
-------------------

metadata
    The meta data for the context.

content
    The HTML rendered from the input file.

html
    The final HTML from the content rendered through a template
'''

def process_content(path):
    '''Process all contents, converting it to HTML.

    **Note: Metadata need to start at the first line of the file, and to have
            ONE newline before the content.**

    :param path: Where the content files are at.
    :type path: string
    :returns: A list of contexts
    '''
    logger.info("Processing content.")
    contents = list()
    # Get list of files
    content_files = get_files(path, '.md')

    # Run through the files
    for filename in content_files:
        # Open it
        with open(filename, 'r') as markdown_file:
            # Create a dictionary for metadata
            metadata = dict()
            metadata['file'] = filename
            logger.debug("Reading markdown from: " + filename)
            # Create an instance of the Markdown processor
            md = markdown.Markdown(extensions=MARKDOWN_EXTENSIONS,
                                   output_format='html5')
            # Convert file to html
            content = md.convert(markdown_file.read())
            # Check for meta data
            if len(md.Meta) == 0:
                raise ContentParserError('No meta data found.')
            # Add meta data from the meta data markdown extension
            metadata.update(md.Meta)
            # Run through extra meta data parsers.
            metadata.update(parsers_run(filename))
            # Create context
            context = dict()
            # Add meta data
            context['metadata'] = metadata
            # Add content
            context['content'] = content
            # Append the content to the list
            contents.append(context)
    return(contents)


def apply_templates(path, contents):
    '''Apply jinja2 templates to content, and write the files.

    :param path: Path to templates
    :type path: string
    :param contents: A list of metadata, content tuples
    :type contents: list
    :returns: List of contexts
    '''
    logger.debug("Applying templates.")
    env = Environment(loader=FileSystemLoader(path))
    result = list()
    # Run through all content
    for context in contents:
        # Use specified template or index.html
        if 'template' in context['metadata'].keys():
            template = context['metadata']['template']
        else:
            logger.warning('Using index.html as template.')
            template = 'index.html'
        # Get template
        tpl = env.get_template(template)

        # Render template
        logger.debug('Rendering template "' + template
                     + '" with "' + context['metadata']['file'] + '"')
        context['html'] = tpl.render(context)
        # Save content to list
        result.append(context)
    return(result)


def run(root):
    '''Process everything and create output files.

    :param root: The root of the site files.
    :type root: string
    '''
    # Process the input files
    contents = process_content(os.path.join(root, SETTINGS['CONTENTDIR']))
    # Apply the templates
    contents = apply_templates(os.path.join(root, 'templates'), contents)
    # Copy and write the output files
    writer.write(os.path.join(root, SETTINGS['CONTENTDIR']), contents)


def close():
    '''
    Perform cleanup.
    '''
    close_log()