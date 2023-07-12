#!/usr/bin/python3
""" Adds a new attribute to an object if it is possible."""


def is_builtin(obj):
    """ Sets checks if a set of attributes
        exist in an object

        Returns:
            true if object is built-in else false"""
    lst = ['__dict__', '__module__']
    if all(elem in dir(obj) for elem in lst):
        return False
    else:
        return True


def add_attribute(obj, name, value):
    """ Sets new attribute to instance of
        custom object.

        Params:
            obj (object): instance
            name (str): name attribute
            value (any): value to set"""
    if is_builtin(obj):
        raise TypeError("can't add new attribute")
    else:
        obj.__setattr__(name, value)
