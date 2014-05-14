'''Running of the content filter extensions.'''
from ssg.contentfilter import CONTENTFILTERS
from ssg.settings import SETTINGS
from ssg.log import logger

# Add generators here
import ssg.contentfilters.localurl


def run(content):
    '''Run all active parsers.'''
    logger.debug("Running content filters.")
    # Run through extra meta data parsers.
    for generator in CONTENTFILTERS:
        if generator.__class__.__name__ in SETTINGS['CONTENTFILTERS']:
            generator.run(content)
