#!/usr/bin/python3
""" Loads a JSON object from a file."""

import json


def load_from_json_file(filename):
    """ Writes JSON to a file

    Params:
        filename (str): name of file."""
    result = ""
    with open(filename, encoding="utf-8") as fd:
        result = fd.read()

    return json.loads(result)
