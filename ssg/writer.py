'''
Everything to do with writing the output files.

:since: 27/04/2014
:author: oblivion
'''
'''
Writer
======

The writers takes care of saving files, and creating directories for the static
site output.

The process is this.
 - Generate output files
 - Copy all other files in the content directory to the output directory
'''
import os
import shutil
from ssg.log import logger
from ssg.settings import SETTINGS
from ssg.tools import get_files


def file_writer(context):
    '''Write a file to the output directory.

    :param context: The context to write.
    :type context: dict
    '''
        # Get path starting from content
    content_path = os.path.join(SETTINGS['ROOTDIR'],
                                SETTINGS['CONTENTDIR'])
    output_filename = os.path.relpath(context['metadata']['file'],
                                      content_path)
    # Strip old extension
    output_filename, _ = os.path.splitext(output_filename)
    # Add new
    output_filename += '.html'
    # Make an absolute path
    output_filename = os.path.join(SETTINGS['ROOTDIR'],
                                   SETTINGS['OUTPUTDIR'],
                                   output_filename)
    # Get the path of the output
    output_path, _ = os.path.split(output_filename)
    logger.debug('Saving to path: ' + output_path)
    # Create directory if it does not exist
    if not os.path.isdir(output_path):
        logger.debug('Creating path: ' + output_path)
        os.makedirs(output_path, mode=0o755)

    with open(output_filename, 'w') as output_file:
        logger.info('Saving to: ' + output_filename)
        output_file.write(context['html'])
    output_file.close()


def copy_file(src, dst):
    '''Copy a file, and create any target directories needed.

    :param src: The source file.
    :type src: String
    :param dst: The destination path.
    :type dst: string
    '''
    # Get content path
    content_path = os.path.join(SETTINGS['ROOTDIR'],
                                SETTINGS['CONTENTDIR'])
    # Get the path relative to the contents dir
    relpath = os.path.relpath(src, content_path)
    # Isolate the path from the filename
    output_path, _ = os.path.split(relpath)
    # Add destination path
    output_path = os.path.join(dst, output_path)
    # Create directory if it does not exist
    if not os.path.isdir(output_path):
        logger.debug('Creating path: ' + output_path)
        os.makedirs(output_path, mode=0o755)
    logger.debug('Copying "' + src + '" to "' + output_path + '"')
    shutil.copy2(src, output_path)


def write(input_path, context_list):
    '''Write and copy all output files into place.

    :param input_path: Path with input files.
    :type input_path: string
    :param context_list: List of context to write.
    :type context_list: list
    '''
    # Create a list of input files
    input_files = get_files(input_path, '.*')
    # Create a list of content files
    content_files = list()
    # Write all content
    logger.info('Saving HTML output.')
    for context in context_list:
        file_writer(context)
        content_files.append(context['metadata']['file'])

    logger.info('Copying static files.')
    # Get output path
    output_path = os.path.join(SETTINGS['ROOTDIR'], SETTINGS['OUTPUTDIR'])
    # Run through and copy the rest of the files
    for filename in input_files:
        if not filename in content_files:
            logger.debug('Copying: ' + filename)
            copy_file(filename, output_path)
