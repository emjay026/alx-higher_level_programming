#!/usr/bin/python3
""" Writes a JSON object to a file."""

import json


def save_to_json_file(my_obj, filename):
    """ Writes JSON to a file

        Params:
            filename (str): name of file
            text (str): contents to write to file """
    num_chars = 0
    result = json.dumps(my_obj)
    with open(filename, 'w') as fd:
        num_chars = fd.write(result)

    return num_chars
