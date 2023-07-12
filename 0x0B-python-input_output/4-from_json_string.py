#!/usr/bin/python3
""" This module contains a function that
    converts a JSON representation of an object
    to python object."""

import json


def from_json_string(my_str):
    """ Converts a JSON object to python
        object.

        Params:
            my_str (JSON): object

        Returns:
            json string."""
    result = json.loads(my_str)
    return result
