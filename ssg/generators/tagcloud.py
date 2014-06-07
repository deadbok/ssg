'''
TagCloudGenerator
==================

Generate a tag cloud and coresponding tag index pages.


Meta data keywords this plug in depends on
------------------------------------------

tags
    A list tags.


Reserved meta data keywords
---------------------------

tagfiles
    Dictionary of index file names for each tag.
'''
import os
from datetime import datetime
from ssg import generator
from ssg.log import logger
from ssg.settings import SETTINGS
from ssg.metadata import ishidden


class TagCloudGenerator(generator.GeneratorBase):
    '''
    Generate a tag cloud and tag index files from a template.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        generator.GeneratorBase.__init__(self)

    def _create_index_metadata(self):
        '''Create metadata and data structure for the index.
        '''
        # Create meta data for index
        # Create a dictionary for metadata
        metadata = dict()
        # Omit page number from first index file
        metadata['src_file'] = ''
        metadata['dst_file'] = os.path.join(SETTINGS['ROOTDIR'],
                                            SETTINGS['OUTPUTDIR'])
        metadata['dst_file'] += '/tagcloud.html'
        metadata['title'] = 'Tag cloud'
        metadata['date'] = datetime.now()
        metadata['template'] = 'tagcloud'
        # Create a contents node for the index
        content = dict()
        # Add meta data
        content['metadata'] = metadata
        # Empty content
        content['content'] = ''
        logger.debug('Autogenerated content: ' + str(content))
        # Add contents to context
        return(content)

    def _create_tag_index(self, context, posts, tag):
        '''Create a tag index from a context.

        :param context:
        :type context:
        :param posts: List of posts in the index.
        :type posts: list
        '''
        logger.debug('Creating categories page for:' + tag)
        # Generate index filename from tag
        dst_file = tag.replace(' ', '_')
        dst_file = '/tag_' + dst_file.replace('/', '-') + '_index.html'
        # Create meta data
        index = self._create_index_metadata()
        # Adjust meta data for the tag index template
        index['metadata']['dst_file'] = os.path.join(SETTINGS['ROOTDIR'],
                                                     SETTINGS['OUTPUTDIR'])
        index['metadata']['dst_file'] += dst_file
        index['metadata']['title'] = 'Tag index: ' + tag
        index['metadata']['template'] = 'tag'
        # Add local context
        index['context'] = {'context': context,
                            'posts': posts,
                            'content': index}

        context.contents.append(index)
        return(dst_file)

    def run(self, context):
        '''Run the generator.

        :param context: The context of the site.
        :type context: ssg.context.Context
        '''
        logger.debug('Running TagCloudGenerator extension.')

        tags = dict()
        # Run through all content and create a dict of tags
        for content in context.contents:
            logger.debug(content['metadata']['title'])
            # Skip pages or hidden
            if content['metadata']['template'] == 'post':
                if ishidden(content['metadata']):
                    logger.debug('Hiding.')
                else:
                    if 'tags' in content['metadata']:
                        # Run through tags
                        for tag in content['metadata']['tags'].split(','):
                            tag = tag.strip().lower()
                            if tag in tags:
                                tags[tag]['items'] += 1
                                tags[tag]['posts'].append(content)
                            else:
                                logger.debug('Adding: ' + tag)
                                tags[tag] = dict()
                                tags[tag]['items'] = 1
                                tags[tag]['posts'] = list()
                                tags[tag]['posts'].append(content)

        # Get maximum number of tags
        max_tags = 1
        for tag in tags.values():
            if max_tags < tag['items']:
                max_tags = tag['items']
        logger.debug('Most used tag used: ' + str(max_tags))
        # Calculate the tag scale factor to get it in 1-10 range.
        tag_scale = 10 / max_tags
        logger.debug('Tag scaling: ' + str(tag_scale))
        # Normalise use range
        for tag in tags.values():
            tag['items'] = int(tag['items'] * tag_scale)

        for tag, data in tags.items():
            tags[tag]['filename'] = self._create_tag_index(context,
                                                           data['posts'],
                                                           tag)
        # Assign index file names to posts
        for content in context.contents:
            # Dictionary to hold the filenames
            filelist = dict()
            # Only posts that are not hidden
            if content['metadata']['template'] == 'post':
                if not ishidden(content['metadata']):
                    logger.debug('Assigning filename to post: ' +
                                 content['metadata']['title'])
                    # Run through all tags
                    if 'tags' in content['metadata']:
                        for tag in content['metadata']['tags'].split(','):
                            tag = tag.lower().strip()
                            filelist[tag] = tags[tag]['filename']
                            logger.debug('"' + tags[tag]['filename'] + '"' +
                                         ' for tag: ' + tag)
            # Assign the file names to the post meta data
            content['metadata']['tagfiles'] = filelist

        logger.debug('Creating tag page.')
        index = self._create_index_metadata()
        # Add local context
        tag_names = sorted(tags)
        index['context'] = {'context': context,
                            'tags': tags,
                            'tag_names': tag_names
                            }

        context.contents.append(index)

# Add TagCloudGenerator to list of parsers
generator.GENERATORS.append(TagCloudGenerator())
