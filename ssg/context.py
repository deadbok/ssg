'''
A context is created for the site. The context contain all information about 
the site.

Variables in the context
-------------------

settings
   All settings used to generate the site. :ref:`configuration'

contents
   A list of all content.


Keys in contents
----------------

metadata
    The meta data for the page.

html_content
    The HTML rendered from the input file.

html
    The final HTML from the content rendered through a template
'''
class Context(object):
    '''
    Class that represent the global context of the site.
    '''

    contents = None
    '''List of all content.'''
    settings = None
    '''Settings for the site.'''
    def __init__(self):
        '''
        Constructor
        '''
        self.contents = list()


CONTEXT = Context()
