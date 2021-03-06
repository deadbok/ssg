'''Running of the meta data parser extensions.'''
from ssg.log import logger
from ssg.metadata import META_PARSERS
from ssg.settings import SETTINGS

# Import extensions
import ssg.metaext.categorymetaparser


def parsers_run(filename):
    '''Run all active parsers.'''
    logger.debug("Running meta data parsers.")
    metadata = dict()
    # Run through extra meta data parsers.
    for parser in META_PARSERS:
        if parser.__class__.__name__ in SETTINGS['METAPARSERS']:
            metadata.update(parser.parse(filename))
    return(metadata)
