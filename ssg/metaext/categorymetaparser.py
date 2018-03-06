"""
CategoryMetaParser
==================

Meta data parser to extract category data from content directories. Each
directory under the content path, becomes a sub- or category. The parser
handles the last directory differently, according to these rules:

- If there are multiply content files in the directory, the name of the
  directory is interpreted as a category.

- If there is only one content file, the directory name is interpreted as the
  title of the content and is discarded.

Reserved meta data keywords
---------------------------

category
    A list of categories.

:since: 26/04/2014
:author: oblivion
"""
import os
from ssg.log import logger
from ssg.settings import SETTINGS
from ssg import metadata
from ssg.tools import get_files


class CategoryMetaParser(metadata.MetaParserBase):
    """Get category meta data from directory names."""

    def __init__(self):
        """Constructor."""
        metadata.MetaParserBase.__init__(self)

    def parse(self, path):
        """
        Parse category from path and return meta data in a dictionary.

        :param path: Path to content.
        :type path: string
        :returns: dict with meta data.
        """
        logger.debug("Parsing category.")
        # Get content directory
        content_dir, _ = os.path.split(path)
        # Get content in directory
        content_files = get_files(content_dir, '*.md')
        # Get content path
        content_path = os.path.join(SETTINGS['ROOTDIR'],
                                    SETTINGS['CONTENTDIR'])
        # Get the path relative to the contents dir
        relpath = os.path.relpath(path, content_path)
        # Isolate the path from the filename
        relpath, _ = os.path.split(relpath)
        # Create category for each sub directory
        category = relpath.split('/')

        if len(content_files) > 1:
            # Multiply content files, treat last directory as a category
            logger.debug("Category: " + str(category))
            # Create dictionary for the meta data
            result = dict()
            # Set category to 'None' if no sub directory
            if category == '':
                result['category'] = 'None'
            else:
                result['category'] = category
            return result
        else:
            # Single content file, treat last directory as a title
            del category[-1]
            logger.debug("Category: " + str(category))
            # Create dictionary for the meta data
            result = dict()
            # Set category to 'None' if no sub directory
            if category == '':
                result['category'] = 'None'
            else:
                result['category'] = category
            return result


# Add CategoriMetaParser to list of parsers
metadata.META_PARSERS.append(CategoryMetaParser())
