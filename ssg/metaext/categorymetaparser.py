'''
CategoryMetaParser
==================

Meta data parser to extract category data from content directories. Each
directory under the content path, becomes a category. E.g.
``python/ssg/somefile.md``, creates "somefile" in the category "ssg" under the
category "python".

Reserved meta data keywords
---------------------------

category
    A list of categories.

:since: 26/04/2014
:author: oblivion
'''
import os
from ssg.log import logger
from ssg.settings import SETTINGS
from ssg import metadata


class CategoryMetaParser(metadata.MetaParserBase):
    '''Get category meta data from directory names.'''
    def __init__(self):
        '''Constructor.'''
        pass

    def parse(self, path):
        '''Parse category from path and return meta data in a dictionary.

        :param path: Path to content.
        :type path: string
        :returns: dict with meta data.
        '''
        logger.debug("Parsing category.")
        # Get content path
        content_path = os.path.join(SETTINGS['ROOTDIR'],
                                    SETTINGS['CONTENTDIR'])
        # Get the path relative to the contents dir
        relpath = os.path.relpath(path, content_path)
        # Isolate the path from the filename
        relpath, _ = os.path.split(relpath)
        # Create category for each sub directory
        category = relpath.split('/')
        logger.debug("Category: " + str(category))
        # Create dictionary for the meta data
        result = dict()
        # Set category to 'None' if no sub directory
        if category == '':
            result['category'] = 'None'
        else:
            result['category'] = category
        return(result)

# Add CategoriMetaParser to list of parsers
metadata.META_PARSERS.append(CategoryMetaParser())
