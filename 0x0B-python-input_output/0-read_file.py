#!/usr/bin/python3
"""Read file function"""

def read_file(filename=""):

    """ with statement used to ensure the file is properly closed after it has been read"""

    """ encoding parameter is set to utf-8"""

    with open(filename, 'r', encoding='utf-8') as f:

        """ read method to read the file"""
        file_contents = f.read()

        """print the file contents"""
        print(file_contents, end="")
