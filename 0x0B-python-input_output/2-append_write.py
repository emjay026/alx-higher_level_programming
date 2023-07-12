#!/usr/bin/python3
""" Writes to a file."""


def append_write(filename="", text=""):
    """ Writes to a file

        Params:
            filename (str): name of file
            text (str): contents to write to file """
    num_chars = 0
    with open(filename, 'a') as fd:
        num_chars = fd.write(text)

    return num_chars
