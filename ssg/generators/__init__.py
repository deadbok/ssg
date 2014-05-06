'''Running of the generator extensions.'''
from ssg.generator import GENERATORS
from ssg.settings import SETTINGS
from ssg.log import logger

# Add generators here
import ssg.generators.blogindex


def run(env, context):
    '''Run all active parsers.'''
    logger.info("Running generators.")
    metadata = dict()
    # Run through extra meta data parsers.
    for generator in GENERATORS:
        if generator.__class__.__name__ in SETTINGS['GENERATORS']:
            generator.run(env, context)
