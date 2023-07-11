#!/usr/bin/python3
""" Module contains MyInt Class.
    that wraps the int object."""


class MyInt(int):
    """ Class that inherets from int and
        overrides some methods."""

    def __ne__(self, other):
        """ negates operator"""
        return super().__eq__(other)

    def __eq__(self, other):
        """ negates operator"""
        return super().__ne__(other)
