'''
LocalURL
========

Translates occurences of the string '$LOCALURL' with the URL of current
content.
If you use this plug in, **every "$" character in the content must be written
"$"**, as LocalURL swallows one.
'''
import os
from string import Template
from ssg import contentfilter
from ssg.log import logger
from ssg.settings import SETTINGS


class LocalURL(contentfilter.ContentFilterBase):
    '''
    Generate an ``index.html`` from a template.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        contentfilter.ContentFilterBase.__init__(self)


    def run(self, content):
        '''Run the generator.

        :param context: The content.
        :type context: dict
        '''
        logger.debug('Running LocalURL extension.')
        localURL, _ = os.path.split(content['metadata']['URL'])
        logger.debug('Local URL: ' + localURL)
        try:
            tmpl = Template(content['content'])
            content['content'] = tmpl.substitute(LOCALURL=localURL)
        except KeyError as exception:
            logger.error('Could not find key ' + str(exception) + '.')
            logger.error('Maybe a missing $ character.')
            raise exception 

# Add LocalURL to list of parsers
contentfilter.CONTENTFILTERS.append(LocalURL())
