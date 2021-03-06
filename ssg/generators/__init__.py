'''Running of the generator extensions.'''
from ssg.generator import GENERATORS
from ssg.settings import SETTINGS
from ssg.log import logger

# Add generators here
import ssg.generators.blogindex
import ssg.generators.categoryindex
import ssg.generators.tagcloud


def run(context):
    '''Run all active parsers.'''
    logger.debug("Running generators.")
    # Run through extra meta data parsers.
    for generator in GENERATORS:
        if generator.__class__.__name__ in SETTINGS['GENERATORS']:
            generator.run(context)
