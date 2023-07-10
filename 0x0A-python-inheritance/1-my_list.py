#!/usr/bin/python3
""" This module contains MyList class
    which inherits from List []"""


class MyList(list):
    """ List wrapper class."""

    def __init(self):
        super().list

    def print_sorted(self):
        """ Function that prints sorted list."""
        mylist = super().copy()
        mylist.sort()
        print(mylist)
