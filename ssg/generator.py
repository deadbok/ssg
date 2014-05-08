'''
A generator passes its output to the Jinja2 for rendering. A generator can
programmatically generate a page, like a global ``index.html``.
'''
from ssg.log import logger
GENERATORS = list()
'''List of active generators.'''


class GeneratorBase(object):
    '''
    Base class for all generators.
    '''
    def __init__(self):
        '''
        Constructor.
        '''
        logger.debug('Constructing GeneratorBase.')

    def run(self, context):
        '''Run the generator.

        :param context: The context of the site.
        :type context: ssg.context.Context
        '''
        logger.warning('Called unimplemented GeneratorBase.run().')
        raise NotImplementedError('Must be implemented in a derived class')
