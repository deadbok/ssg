'''
LocalURL
========

Translates occurences of the string '$LOCALURL' with the URL of current
content.
If you use this plug in, **every "$" character in the content must be written
"$$"**, as LocalURL swallows one.
'''
import os
from string import Template
from ssg import contentfilter
from ssg.log import logger
from ssg.settings import SETTINGS

class MissingDollarError(RuntimeError):
    '''
    Missing dollar sign
    '''
    pass


class LocalURL(contentfilter.ContentFilterBase):
    '''
    Generate an ``index.html`` from a template.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        contentfilter.ContentFilterBase.__init__(self)
        
    def __check_tmpl_vars(self, content):
        '''
        Check for stray single dollar characters.

        :param content: List of content lines.
        :type content: list
        '''
        logger.debug('Checking content for stray dollars')
        n_line = 1
        for line in content.split('\n'):
            logger.debug('Template line {}: {}'.format(n_line, line))
            index = line.find('$')
            while index is not -1:
                logger.debug('Dollar at {}: {}'.format(index, line[index:]))
                if (line.find('LOCALURL', index, index+9)) is -1 and (line.find('$', index + 1, index + 2) is -1):
                       logger.debug('Single dollar at {}: {}'.format(index, line[index-2:]))
                       logger.error('Single $ character detected in line {},{}: "{}"'.format(n_line, index, line))
                       raise MissingDollarError('Stray single dollar character')
                else:
                    index += 2
                    if index < len(line):
                        index = line.find('$', index)
                    else:
                        index = -1
            n_line += 1

    def run(self, content):
        '''Run the generator.

        :param context: The content.
        :type context: dict
        '''
        logger.debug('Running LocalURL extension.')
        localURL, _ = os.path.split(content['metadata']['URL'])
        logger.debug('Local URL: ' + localURL)
        self.__check_tmpl_vars(content['content'])
        try:
            tmpl = Template(content['content'])
            content['content'] = tmpl.substitute(LOCALURL=localURL)
        except KeyError as exception:
            logger.error('Could not find key ' + str(exception) + '.')
            logger.error('Maybe a missing $ character.')
            raise exception

# Add LocalURL to list of parsers
contentfilter.CONTENTFILTERS.append(LocalURL())
