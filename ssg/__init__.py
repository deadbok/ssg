'''
Main routines for the Static Site Generator.
'''

import logging
import os
import codecs
import markdown
from ssg import writer
from jinja2 import Environment, FileSystemLoader, TemplateSyntaxError
from jinja2 import TemplateError
from ssg.log import logger, init_file_log, init_console_log, close_log
from ssg.metaext import parsers_run
from ssg import settings
from ssg.settings import SETTINGS, write_config
from ssg.tools import get_files, get_datetime, die
from ssg.context import CONTEXT
from ssg import generators
from ssg import contentfilters
# Markdown extensions
from ssg.markdownext.figure import FigureExtension


__version__ = '0.0.4'
configs = {}
# Instantiate Markdown extensions
figure = FigureExtension(configs=configs)

# Extra extensions
# Meta-data extension
# Table of Contents extension
# Figure extension
MARKDOWN_EXTENSIONS = [ 'markdown.extensions.extra',
                        'markdown.extensions.meta',
                        'markdown.extensions.toc',
                        figure]
'''Markdown extension to use.'''

DEBUG = False


class ContentParserError(RuntimeError):
    '''
    The client has received an unexpected response
    '''
    pass


def init(debug=False, root=None):
    '''Initialise ssg

    :param debug: True enables debugging to console
    :type debug: bool
    :param root: Root directory of the site
    :type root: string
    '''
    global DEBUG
    # Init logging to file
    init_file_log(logging.DEBUG)
    # Set the console logging level
    if debug:
        init_console_log(logging.DEBUG)
        DEBUG = True
    else:
        init_console_log(logging.INFO)
    # Init settings placeholder
    settings.init(root)


def _get_url(metadata):
    '''Get the final URL of the rendered html on the site.

    :param metadata: Meta data to use. *src_file* key must be present.
    :type metadata: dict
    '''
    logger.debug('Generating URL from: ' + str(metadata))
    # Start with the site URL
    url = SETTINGS['SITEURL'] + '/'
    # Get path starting from content
    content_path = os.path.join(SETTINGS['ROOTDIR'],
                                SETTINGS['CONTENTDIR'])
    output_filename = os.path.relpath(metadata['src_file'],
                                      content_path)
    # Strip old extension
    output_filename, _ = os.path.splitext(output_filename)
    # Add new
    output_filename += '.html'
    # Add the filename to the URL
    url += output_filename
    logger.debug('URL: ' + url)
    return url


def _new_metadata(filename, md):
    '''
    Create new meta data from a Markdown file.

    :param filename: The full path of the source Markdown file.
    :type filename: string
    :param md: An instance of the Markdown preprocessor
    :type md: markdown.Markdown
    '''

    # Create a dictionary for meta data
    metadata = dict()
    metadata['src_file'] = filename
    # Create output file path and name
    # Get path starting from content
    content_path = os.path.join(SETTINGS['ROOTDIR'],
                                SETTINGS['CONTENTDIR'])
    output_filename = os.path.relpath(metadata['src_file'],
                                      content_path)
    # Strip old extension
    output_filename, _ = os.path.splitext(output_filename)
    # Add new
    output_filename += '.html'
    # Make an absolute path
    output_filename = os.path.join(SETTINGS['ROOTDIR'],
                                   SETTINGS['OUTPUTDIR'],
                                   output_filename)
    # Save output file name
    metadata['dst_file'] = output_filename
    metadata['URL'] = _get_url(metadata)
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
    return metadata


def process_content(path, context):
    '''Process all contents, converting it to HTML.

    *Metadata need to start at the first line of the file, and to have ONE
    newline before the content.*

    :param path: Where the content files are at.
    :type path: string
    :returns: A list of contexts
    '''
    logger.info("Processing content.")
    # Get list of files
    content_files = get_files(path, '.md')

    # Run through the files
    for filename in content_files:
        try:
            # Open it
            with codecs.open(filename, encoding='utf-8') as markdown_file:
                logger.info("Reading: " + filename)
                # Create an instance of the Markdown processor
                md = markdown.Markdown(extensions=MARKDOWN_EXTENSIONS,
                                       output_format='html5')
                # Convert file to html
                html_content = md.convert(markdown_file.read())
                # Create meta data
                metadata = _new_metadata(filename, md)
                # Create content
                content = dict()
                # Add meta data
                content['metadata'] = metadata
                # Add content
                content['content'] = html_content
                # Run content filters on content
                contentfilters.run(content)
                # Append the content to the list
                context.contents.append(content)
        except Exception as exception:
            if DEBUG:
                logger.exception('Exception reading file: ' + filename)
            else:
                logger.error('Exception reading file: ' + filename)
            raise exception
    return(context)


def sanity_checks(context):
    '''Checks to see if the templates and content actually parses.

    :param context:
    :type context:
    '''
    logger.debug("Running sanity checks on input.")
    for content in context.contents:
        # Check if template is set
        if 'template' not in content['metadata']:
            raise ContentParserError('Missing template in: ' +
                                     content['metadata']['src_file'])
        if 'title' not in content['metadata']:
            raise ContentParserError('Missing title in: ' +
                                     content['metadata']['src_file'])


def apply_templates(path, context):
    '''
    Apply jinja2 templates to content, and write the files.

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
            if content['metadata']['src_file'] != '':
                logger.info("Rendering " + content['metadata']['src_file'])
            logger.debug('Rendering template "' + template +
                         '" with "' + content['metadata']['src_file'] + '"')
            content['html'] = tpl.render(local_context)
    except TemplateSyntaxError as exception:
        logger.error('Jinja2 syntax error:')
        logger.error('In ' + exception.name + ' line number :' +
                     str(exception.lineno))
        logger.error(exception.filename)
        raise exception
    except TemplateError as exception:
        logger.error('Jinja2 syntax error:')
        logger.error('Template: ' + content['metadata']['template'])
        logger.error('Destination: ' + content['metadata']['dst_file'])
        raise exception
    return(context)


def create_empty_site(path=None):
    '''
    Create the skeleton and config file for a new site.

    :param path: Root path of the new site. Default is current directory.
    :type path: string
    '''
    # Defaults to current directory
    if path is None:
        path = os.getcwd()
    # Write a shiny new configuration file
    write_config(path)

    # Create directories
    os.mkdir(os.path.join(SETTINGS['ROOTDIR'], SETTINGS['CONTENTDIR']))
    os.mkdir(os.path.join(SETTINGS['ROOTDIR'], SETTINGS['TEMPLATEDIR']))
    os.mkdir(os.path.join(SETTINGS['ROOTDIR'], SETTINGS['OUTPUTDIR']))


def run(update):
    '''Process everything and create output files.

    :param update: Only write updated files.
    :type update: bool
    '''
    global CONTEXT, DEBUG
    # Add settings to global context
    CONTEXT.settings = SETTINGS
    try:
        # Process the input files
        CONTEXT = process_content(os.path.join(SETTINGS['ROOTDIR'],
                                               SETTINGS['CONTENTDIR']),
                                  CONTEXT)
        # Template and content sanity checks
        sanity_checks(CONTEXT)
        # Apply the templates
        CONTEXT = apply_templates(os.path.join(SETTINGS['ROOTDIR'],
                                               SETTINGS['TEMPLATEDIR']),
                                  CONTEXT)
        # Copy and write the output files
        writer.write(os.path.join(SETTINGS['ROOTDIR'], SETTINGS['CONTENTDIR']),
                     CONTEXT,
                     update)
    except Exception as exception:
        logger.error(str(exception))
        if DEBUG:
            raise exception
        die()


def close():
    '''
    Perform cleanup.
    '''
    close_log()
