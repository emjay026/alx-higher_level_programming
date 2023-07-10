#!/usr/bin/python3
""" Module contains is_same_class function."""


def is_same_class(obj, a_class):
    """ Checks if obj is an instance of a_class.

    Params:
        obj (any object): an object instance.
        a_class (any class): a class"""
    return isinstance(obj, a_class)
