#!/usr/bin/python3
""" Module contains is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """ Function checks if obj is a child of a_class.

    Params:
        obj (any object): an object instance.
        a_class (any class): a class"""
    return issubclass(type(obj), a_class)
