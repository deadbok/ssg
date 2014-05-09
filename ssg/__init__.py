'''
Main routines for the Static Site Generator.

:author: deadbok
'''

import logging
import os
import markdown
from ssg import writer
from jinja2 import Environment, FileSystemLoader, TemplateSyntaxError
from ssg.log import logger, init_file_log, init_console_log, close_log
from ssg.metaext import parsers_run
from ssg import settings
from ssg.settings import SETTINGS
from ssg.tools import get_files, get_datetime
from ssg.context import CONTEXT
from ssg import generators

__version__ = '0.0.2'

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


def _get_url(metadata):
    '''Get the final URL of the rendered html on the site.

    :param metadata: Meta data to use. *file* key must be present.
    :type metadata: dict
    '''
    logger.debug('Generating URL from: ' + str(metadata))
    # Start with the site URL
    url = SETTINGS['SITEURL'] + '/'
    # Get path starting from content
    content_path = os.path.join(SETTINGS['ROOTDIR'],
                                SETTINGS['CONTENTDIR'])
    output_filename = os.path.relpath(metadata['file'],
                                      content_path)
    # Strip old extension
    output_filename, _ = os.path.splitext(output_filename)
    # Add new
    output_filename += '.html'

    url += output_filename
    logger.debug('URL: ' + url)
    return(url)


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
            # Create a dictionary for meta data
            metadata = dict()
            metadata['file'] = filename
            metadata['URL'] = _get_url(metadata)

            logger.info("Reading: " + filename)
            # Create an instance of the Markdown processor
            md = markdown.Markdown(extensions=MARKDOWN_EXTENSIONS,
                                   output_format='html5')
            # Convert file to html
            html_content = md.convert(markdown_file.read())
            # Check for meta data
            if len(md.Meta) == 0:
                raise ContentParserError('No meta data found.')
            # Splice the lines together
            for key, item in md.Meta.items():
                item = ''.join(item)
                # Add meta data from the meta data markdown extension
                metadata[key] = item
            # Get python datetime from the one in the content meta data
            if 'date' in metadata.keys():
                metadata['date'] = get_datetime(metadata['date'])
            # Run through extra meta data parsers.
            metadata.update(parsers_run(filename))
            # Create content
            content = dict()
            # Add meta data
            content['metadata'] = metadata
            # Add content
            content['content'] = html_content
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
    logger.info('Applying templates.')
    env = Environment(loader=FileSystemLoader(path))
    # Run generator extensions
    generators.run(context)
    # Run through all content
    try:
        logger.info('Applying to contents.')
        for content in context.contents:
            # Use specified template or index.html
            if 'template' in content['metadata'].keys():
                template = content['metadata']['template'] + '.html'
            else:
                template = 'page.html'
            logger.debug('Using "' + template + '" as template.')
            # Get template
            tpl = env.get_template(template)
            # Use default context if none is set
            if 'context' in content.keys():
                local_context = content['context']
            else:
                local_context = {'context': context, 'content': content}
            # Render template
            logger.debug('Rendering template "' + template
                         + '" with "' + content['metadata']['file'] + '"')
            content['html'] = tpl.render(local_context)
    except TemplateSyntaxError as exception:
        logger.error('Jinja2 syntax error:')
        logger.error(exception.message)
        logger.error('In ' + exception.name + ' line number :' + str(exception.lineno))
        logger.error(exception.filename)
        exit(1)
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
