'''Meta data parser to extract category data from content directories.

:since 26/04/2014
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
        content_path = SETTINGS['ROOTDIR'] + '/' + SETTINGS['CONTENTDIR']
        path = os.path.relpath(path, content_path)
        path, _ = os.path.split(path)
        category = path.split('/')
        logger.debug("Category: " + str(category))
        metadata = dict()
        metadata['category'] = category
        return(metadata)

# Add CategoriMetaParser to list of parsers
metadata.META_PARSERS.append(CategoryMetaParser())
