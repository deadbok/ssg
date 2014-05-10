'''
Figure Markdown extension
=========================

This extension adds an inline element for creating figures.

Example::

    !{Some Caption}(image.jpg)

Renders as::

    div class="w-300px img-responsive figure align-center">
        <img alt="Some Captiont" class="img-responsive" src="image.jpg">
        <a href="image.jpg">Some Caption</a>
    </div>
'''
from __future__ import absolute_import
from __future__ import unicode_literals
from markdown import Extension
from markdown.inlinepatterns import LinkPattern
from markdown.util import etree
from ssg.log import logger

FIGURE_RE = r'\!{([\w\d_\s-]+)}\(([$/\.\w\d_-]+)\)'


class FigureExtension(Extension):
    '''Class to register the figure extension.'''
    def extendMarkdown(self, md, md_globals):
        # append to end of inline patterns
        logger.debug('Adding figure Markdown extension.')
        md.inlinePatterns.add('figure',
                              FigurePattern(FIGURE_RE, md),
                              "<not_strong")


class FigurePattern(LinkPattern):
    '''Figure extension for Markdown.'''
    def handleMatch(self, m):
        logger.debug('Found figure: ' + m.group(2))
        # Create a div styled into hell
        # TODO: Make classes configurable
        div = etree.Element('div',
                            {'class': 'imgwidth figure'})
        # Crete the image
        # TODO: Make classes configurable
        img = etree.SubElement(div, 'img', {'class': 'img-responsive'})
        # Get the src attribute
        src_parts = m.group(3).split()
        if src_parts:
            src = src_parts[0]
            if src[0] == "<" and src[-1] == ">":
                src = src[1:-1]
            img.set('src', self.sanitize_url(self.unescape(src)))
        else:
            img.set('src', "")
        # Set alt attribute
        img.set('alt', m.group(2))
        # Create a link to the full image, with the alt text as a caption
        link = etree.SubElement(div, 'a')
        link.text = m.group(2)
        link.set('href', self.sanitize_url(self.unescape(src)))
        return div


def makeExtension(configs=None):
    return FigureExtension(configs=configs)
