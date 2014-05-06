'''
BlogIndexGenerator
==================

Generate an ``index.html`` file from a template of the same name. This is
useful for blogs and pages for indexing articles, creating the index on the
fly.

:since: 06/05/2014
:author: oblivion
'''
from ssg import generator
from ssg.log import logger
from ssg.settings import SETTINGS
from ssg import metadata


class BlogIndexGenerator(generator.GeneratorBase):
    '''
    Generate an ``index.html`` from a template.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        generator.GeneratorBase.__init__(self)

    def run(self, env, context):
        '''Run the generator.

        :param env: Jinja2 environment.
        :type env: Jinja2 environment
        :param context: The context of the site.
        :type context: ssg.context.Context
        '''
        logger.debug('Running BlogIndexGenerator extension.')
        # Run with index.html template
        template = 'index.html'
        tpl = env.get_template(template)

        # Create meta data for index
        # Create a dictionary for metadata
        metadata = dict()
        metadata['file'] = SETTINGS['CONTENTDIR'] + '/index.html'
        metadata['title'] = 'index'
        metadata['type'] = 'index'
        # Create a contents node for the index
        content = dict()
        # Add meta data
        content['metadata'] = metadata
        # Empty content
        content['content'] = ''
        logger.debug('Autogenerated content: ' + str(content))

        # Render template
        logger.debug('Rendering index.html')
        index = tpl.render(context=context, content=content)

        # Final html
        content['html'] = index
        # Add contents to context
        context.contents.append(content)

# Add CategoriMetaParser to list of parsers
generator.GENERATORS.append(BlogIndexGenerator())
