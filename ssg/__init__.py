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
from ssg.context import CONTEXT

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


def process_content(path, context):
    '''Process all contents, converting it to HTML.

    **Note: Metadata need to start at the first line of the file, and to have
            ONE newline before the content.**

    :param path: Where the content files are at.
    :type path: string
    :returns: A list of contexts
    '''
    logger.info("Processing content.")
    # Get list of files
    content_files = get_files(path, '.md')

    # Run through the files
    for filename in content_files:
        # Open it
        with open(filename, 'r') as markdown_file:
            # Create a dictionary for metadata
            metadata = dict()
            metadata['file'] = filename
            logger.info("Reading: " + filename)
            # Create an instance of the Markdown processor
            md = markdown.Markdown(extensions=MARKDOWN_EXTENSIONS,
                                   output_format='html5')
            # Convert file to html
            html_content = md.convert(markdown_file.read())
            # Check for meta data
            if len(md.Meta) == 0:
                raise ContentParserError('No meta data found.')
            # Add meta data from the meta data markdown extension
            metadata.update(md.Meta)
            # Run through extra meta data parsers.
            metadata.update(parsers_run(filename))
            # Create content
            content = dict()
            # Add meta data
            content['metadata'] = metadata
            # Add content
            content['html_content'] = html_content
            # Append the content to the list
            context.contents.append(content)
    return(context)


def apply_templates(path, context):
    '''Apply jinja2 templates to content, and write the files.

    :param path: Path to templates
    :type path: string
    :param contents: A list of metadata, content tuples
    :type contents: list
    :returns: List of contexts
    '''
    logger.info("Applying templates.")
    env = Environment(loader=FileSystemLoader(path))
    # Run through all content
    for content in context.contents:
        # Use specified template or index.html
        if 'template' in content['metadata'].keys():
            template = content['metadata']['template'][0] + '.html'
        else:
            logger.warning('Using page.html as template.')
            template = 'page.html'
        # Get template
        tpl = env.get_template(template)

        # Render template
        logger.debug('Rendering template "' + template
                     + '" with "' + content['metadata']['file'] + '"')
        content['html'] = tpl.render(context=context, content=content)
    return(context)


def run(root):
    '''Process everything and create output files.

    :param root: The root of the site files.
    :type root: string
    '''
    global CONTEXT
    # Add settings to global context
    CONTEXT.settings = SETTINGS
    # Process the input files
    CONTEXT = process_content(os.path.join(root, SETTINGS['CONTENTDIR']), CONTEXT)
    # Apply the templates
    CONTEXT = apply_templates(os.path.join(root, 'templates'), CONTEXT)
    # Copy and write the output files
    writer.write(os.path.join(root, SETTINGS['CONTENTDIR']), CONTEXT)


def close():
    '''
    Perform cleanup.
    '''
    close_log()
