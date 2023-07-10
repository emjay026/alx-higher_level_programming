#!/usr/bin/python3
""" This module contains MyList class"""


class MyList(list):
    """ List wrapper class."""

    def __init(self):
        """ Funtion that initializes
            an instance of MyList"""
        super().list

    def print_sorted(self):
        """ Function that prints sorted list."""
        mylist = super().copy()
        mylist.sort()
        print(mylist)
