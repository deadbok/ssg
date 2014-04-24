'''

@since 23/04/2014
@author: oblivion
'''


class BaseReader(object):
    """Base class to read content files."""
    file_extensions = ['static']
    extensions = None

    def __init__(self):
        pass

    def read(self, filename:
        """Parser that does nothing."""
        content = None
        metadata = {}
        return content, metadata