#!/usr/bin/python3
""" Module contains inherits_from function."""


def inherits_from(obj, a_class):
    """ Checks if obj is an instance of a_class.

    Params:
        obj (any object): an object instance.
        a_class (any class): a class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
