import os

__version__ = '0.0.1'


def get_content_files(path, extension):
    """Get a list of files with extension from path an subdirectories."""
    filelist = list()

    for entry in os.listdir(path):
        #Ignore . and ..
        if not (entry.find('.') == 0):
            filename = path + "/" + entry
            #Process subdirectories
            if os.path.isdir(filename):
                filelist.append(get_content_files(filename, extension))
            else:
                if (os.path.splitext(path) == extension):
                    filelist.append(