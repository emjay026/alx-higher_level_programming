#!/usr/bin/python3
"""Implements LockedClass"""


class LockedClass:
    """new instance attribute must be called first_name."""
    def __setattr__(self, name, value):
        """dynamically creates attribute

        Params:
            name (string):
            value ():"""

        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '"
                                 + name + "'")
        self.__dict__[name] = value
