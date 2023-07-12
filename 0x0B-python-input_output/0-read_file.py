#!/usr/bin/python3
""" This module implements a function
    that reads in a file and prints it
    out to stdout."""


def read_file(filename=""):
    """ Opens and reads a file.

        Param:
            filename (str): name of file"""
    with open(filename, encoding="utf-8") as fd:
        print(fd.read())
