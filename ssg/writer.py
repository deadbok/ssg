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
from ssg.tools import get_files, get_dirs, die


def _create_dir(path):
    '''
    Create a directory (and direcotries below) if they are not already there.

    :param path: Path of the directory to create
    :type path: string
    '''
    if not os.path.isdir(path):
        logger.debug('Creating path: ' + path)
        os.makedirs(path, mode=0o755)


def _check_updated(context):
    '''
    Check which files need updating.

    :param context: Site context.
    :type context: ssg.context.Context
    '''
    logger.debug('Checking which files need updating.')
    # Assume nothin' needs to be updated
    content_upd = False
    # Get template modification times
    template_files = get_files(os.path.join(SETTINGS['ROOTDIR'],
                                            SETTINGS['TEMPLATEDIR']),
                               '.html')
    newest_template = 0
    for fullpath in template_files:
        mtime = os.stat(fullpath).st_mtime
        if newest_template < mtime:
            newest_template = mtime

    # Get the config file modification time
    config_time = os.stat(SETTINGS['ROOTDIR'] + '/config.py').st_mtime
    # Update all content older than the newest template
    # Get changed content
    # Run through all content.
    for content in context.contents:
        # If file has a source it is not generated.
        if not content['metadata']['src_file'] == '':
            logger.debug('Checking: ' + content['metadata']['src_file'])
            # Get modification time of source and destination.
            src_mtime = os.stat(content['metadata']['src_file']).st_mtime
            if os.path.isfile(content['metadata']['dst_file']):
                dst_mtime = os.stat(content['metadata']['dst_file']).st_mtime
            else:
                # Make sure the target is updated if it does not exist
                dst_mtime = 0
            logger.debug('Source mtime: ' + str(src_mtime))
            logger.debug('Destination mtime: ' + str(dst_mtime))
            logger.debug('Newest template mtime: ' + str(newest_template))
            # Check if destination is older than newest template
            if dst_mtime < config_time:
                logger.debug('Destination needs updating. Config change.')
                # Content updated
                content_upd = True
                content['metadata']['updated'] = True
            # Check if destination is older than newest template
            if dst_mtime < newest_template:
                logger.debug('Destination needs updating. Template change.')
                # Content updated
                content_upd = True
                content['metadata']['updated'] = True
            # Check if source is newer that destination
            if src_mtime > dst_mtime:
                logger.debug('Destination needs updating. Source change.')
                # Content updated
                content_upd = True
                content['metadata']['updated'] = True
            else:
                if 'updated' not in content['metadata'].keys():
                    content['metadata']['updated'] = False
            # Check if template is newer than
    # If content is updated write generated pages.
    # Run through all content.
    for content in context.contents:
        # If file has no source it is generated
        if content['metadata']['src_file'] == '':
            if content_upd:
                logger.debug('"' + content['metadata']['title'] +
                             '" needs updating.')
                content['metadata']['updated'] = True
            else:
                content['metadata']['updated'] = False


def file_writer(content):
    '''Write a file to the output directory.

    :param content: The content to write.
    :type content: dict
    :return: Filename of the written file.
    :rtype: string
    '''
    # Generate ouput file name if none is set
    if content['metadata']['dst_file'] == '':
        logger.error('No destination file name for: ' +
                     content['metadata']['title'])
        die()
    else:
        output_filename = content['metadata']['dst_file']
    # Get the path of the output
    output_path, _ = os.path.split(output_filename)
    logger.debug('Saving to path: ' + output_path)
    _create_dir(output_path)

    with open(output_filename, 'w', encoding='utf8') as output_file:
        logger.info('Saving to: ' + output_filename)
        output_file.write(content['html'])
    output_file.close()
    return output_filename


def copy_file(src, dst, update=True):
    '''Copy a file, and create any target directories needed.

    :param src: The source file.
    :type src: string
    :param dst: The destination path.
    :type dst: string
    :param update: Only copy updated files.
    :type update: bool
    :return: Filename of the destination.
    :rtype: string
    '''
    # Get source file modification time
    src_mtime = os.stat(src).st_mtime
    # Get content path
    content_path = os.path.join(SETTINGS['ROOTDIR'],
                                SETTINGS['CONTENTDIR'])
    # Get the path relative to the contents dir
    relpath = os.path.relpath(src, content_path)
    # Isolate the path from the file name
    relpath, _ = os.path.split(relpath)
    output_file = os.path.join(dst, relpath, os.path.basename(src))
    if os.path.isfile(output_file):
        dst_mtime = os.stat(output_file).st_mtime
    else:
        # Make sure the target is updated
        dst_mtime = 0
    # Check if source is newer that destination
    if (src_mtime > dst_mtime) or (update is False):
        # Add destination path
        output_path = os.path.join(dst, relpath)
        _create_dir(output_path)
        logger.info('Copying "' + src + '" to "' + output_path + '"')
        return shutil.copy2(src, output_path)
    else:
        logger.debug('Skipping: ' + src)
        # Return destination anyway, to have a list of supposedly copied files
        return output_file


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


def write(input_path, context, update=True):
    '''Write and copy all output files into place.

    :param input_path: Path with input files.
    :type input_path: string
    :param context: Context to write.
    :type context: dict
    :param update: Only write updated files.
    :type update: bool
    '''
    # Create a list of input files
    input_files = get_files(input_path, '.*')
    # Create a list of written files
    written_files = list()
    if update:
        # Check which needs an update.
        _check_updated(context)
    else:
        # Update all
        for content in context.contents:
            content['metadata']['updated'] = True
    # Write all content
    logger.info('Saving HTML output.')
    for content in context.contents:
        # Check if file need to be writte.
        if content['metadata']['updated']:
            written_files.append(file_writer(content).strip())
        else:
            # Add to list to prevent deletion
            written_files.append(content['metadata']['dst_file'])

    logger.info('Copying static files.')
    # Get output path
    output_path = os.path.join(SETTINGS['ROOTDIR'], SETTINGS['OUTPUTDIR'])
    # Run through and copy the rest of the files
    for filename in input_files:
        # Only copy html sources if configured
        _, ext = os.path.splitext(filename)
        if ext.lower() == '.md':
            if SETTINGS['COPYSOURCES']:
                written_files.append(copy_file(filename, output_path, update))
            else:
                logger.debug('Skipping: ' + filename)
        # Skip duplicates of files created by ssg.
        elif filename not in written_files:
            # Write other files.
            written_files.append(copy_file(filename, output_path, update))
        else:
            logger.debug('Skipping: ' + filename)
    # Remove files that are no longer in the source
    cleanup_destination(output_path, written_files)
