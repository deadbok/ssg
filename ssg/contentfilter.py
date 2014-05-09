'''
Content filters, do some filtering or processing of the HTML output from the
output of the conversion process, from Markdown. Meta data and content are
available at this stage.
'''
from ssg.log import logger
CONTENTFILTERS = list()
'''List of active content filters.'''


class ContentFilterBase(object):
    '''
    Base class for all content filters.
    '''
    def __init__(self):
        '''
        Constructor.
        '''
        logger.debug('Constructing ContentFilterBase.')

    def run(self, content):
        '''Run the generator.

        :param context: The content of the rendered Markdown
        :type context: dict
        '''
        logger.warning('Called unimplemented ContentFilterBase.run().')
        raise NotImplementedError('Must be implemented in a derived class')
