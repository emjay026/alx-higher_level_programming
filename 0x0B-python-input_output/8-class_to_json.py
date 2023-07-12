#!/usr/bin/python3
""" Returns the dictionary description
    with simple data structure."""


def class_to_json(obj):
    """ returns a dictionary.

        Params:
            a class instance
        Returns:
            dictionary"""
    return obj.__dict__
