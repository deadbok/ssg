from ssg.log import logger
from ssg.metadata import META_PARSERS
from ssg.settings import SETTINGS
import ssg.metaext.categorymetaparser


def parsers_run(filename):
    '''Run all active parsers.'''
    logger.debug("Running meta data parsers.")
    metadata = dict()
    # Run through extra meta data parsers.
    for parser in META_PARSERS:
        if parser.__class__.__name__ in SETTINGS['METAEXTS']:
            metadata.update(parser.parse(filename))
    return(metadata)