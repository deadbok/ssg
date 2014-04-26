'''
Parsers for meta data.

:since: 25/04/2014
:author: oblivion
'''
META_PARSERS = list()
'''List of active meta data parsers.'''


class MetaParserBase(object):
    '''Base class for metadata parsers. '''
    def __init__(self):
        '''Constructor'''
        pass

    def parse(self, path):
        '''Parse something and return meta data in a dictionary.

        :param path: Path to content.
        :type path: string
        :returns: dict with meta data.
        '''
        raise NotImplementedError('Must be implemented in a derived class')
