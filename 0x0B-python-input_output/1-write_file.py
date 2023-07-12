#!/usr/bin/python3
""" Writes to a file."""


def write_file(filename="", text=""):
    """ Writes to a file

        Params:
            filename (str): name of file
            text (str): contents to write to file """
    num_chars = 0
    with open(filename, 'w') as fd:
        num_chars = fd.write(text)

    return num_chars
