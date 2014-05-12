'''
The writers takes care of creating the final static output.

The process is this.
 - Generate output files from a list of contexts.
 - Copy all other files in the content directory to the output directory.
 - Delete *anything* that is not present in the content directory
'''
import os
import shutil
from ssg.log import logger
from ssg.settings import SETTINGS
from ssg.tools import get_files, get_dirs


def file_writer(content):
    '''Write a file to the output directory.

    :param content: The content to write.
    :type content: dict
    :return: Filename of the written file.
    :rtype: string
    '''
    # Get path starting from content
    content_path = os.path.join(SETTINGS['ROOTDIR'],
                                SETTINGS['CONTENTDIR'])
    output_filename = os.path.relpath(content['metadata']['file'],
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
        output_file.write(content['html'])
    output_file.close()
    return(output_filename)


def copy_file(src, dst):
    '''Copy a file, and create any target directories needed.

    :param src: The source file.
    :type src: string
    :param dst: The destination path.
    :type dst: string
    :return: Filename of the destination.
    :rtype: string
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
    logger.info('Copying "' + src + '" to "' + output_path + '"')
    return(shutil.copy2(src, output_path))


def cleanup_destination(output_path, written_files):
    '''Delete any files in the destination directory that are no longer in
    the source directory. The algorithm replaces ".md" with ".html."

    :param output_path: Path to output files.
    :type output_path: string
    :param written_files: list of files that was created by this run.
    :type written_files: list
    :return: Filename of the destination.
    :rtype: string
    '''
    logger.info('Cleaning output directory.')
    # Get files in output path
    logger.debug("Getting all files in the output path.")
    current_files = get_files(output_path, '.*')
    # Create a list of all files to delete
    delete_list = list()
    # Run through all source filed
    for filename in current_files:
        # Check if file was created by this run
        if filename not in written_files:
            logger.debug('Adding: ' + filename)
            delete_list.append(filename)
        else:
            logger.debug('Skipping: ' + filename)
    # Delete the files
    for filename in delete_list:
        logger.info('Deleting file: ' + filename)
        os.remove(filename)

    # Move on to cleaning up any deleted directories.
    # Get directories in output output_dir.
    dst_dirs = get_dirs(output_path + '/')
    # Create a list for the directories to delete
    dirlist = list()
    # Run trough all directories in the output
    for dst_dir in dst_dirs:
        if os.path.isdir(dst_dir):
            # Get path starting from content
            output_path = os.path.join(SETTINGS['ROOTDIR'],
                                       SETTINGS['OUTPUTDIR'])
            reldir = os.path.relpath(dst_dir, output_path)
            content_path = os.path.join(SETTINGS['ROOTDIR'],
                                       SETTINGS['CONTENTDIR'],
                                       reldir)
            if not os.path.isdir(content_path):
                dirlist.append(dst_dir)
    # Delete directories backwards to make sure subdirectories go first
    for output_dir in reversed(dirlist):
        # Do not try to delete the output directory
        if not output_dir == os.path.join(SETTINGS['ROOTDIR'],
                                   SETTINGS['OUTPUTDIR']):
            logger.info('Deleting directory: ' + output_dir)
            os.rmdir(output_dir)


def write(input_path, context):
    '''Write and copy all output files into place.

    :param input_path: Path with input files.
    :type input_path: string
    :param context: Context to write.
    :type context: dict
    '''
    # Create a list of input files
    input_files = get_files(input_path, '.*')
    # Create a list of written files
    written_files = list()
    # Write all content
    logger.info('Saving HTML output.')
    for content in context.contents:
        written_files.append(file_writer(content).strip())

    logger.info('Copying static files.')
    # Get output path
    output_path = os.path.join(SETTINGS['ROOTDIR'], SETTINGS['OUTPUTDIR'])
    # Run through and copy the rest of the files
    for filename in input_files:
        # Only copy html sources if configured
        _, ext = os.path.splitext(filename)
        if (ext.lower() == '.md'):
            if (SETTINGS['COPYSOURCES']):
                written_files.append(copy_file(filename, output_path))
            else:
                logger.debug('Skipping: ' + filename)
        # Skip duplicates of files created by ssg.
        elif not filename in written_files:
            # Write other files.
            written_files.append(copy_file(filename, output_path))
        else:
            logger.debug('Skipping: ' + filename)
    # Remove files that are no longer in the source
    cleanup_destination(output_path, written_files)
