#!/usr/bin/python3
""" Reads in arguments from the command line
    and saves then to a .json file."""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"


def load(filename):
    """ loads json from file
        or creates json file if DNE.

        Params:
            filename (str): file name."""
    result = ""
    try:
        result = load_from_json_file(filename)
    except FileNotFoundError:
        save_to_json_file([], filename)
    return result


def add(list_obj, list_):
    """ appends items to list.

        Params:
            list (list): """
    for item in list_:
        list_obj.append(item)


list_obj = load(filename)

if len(sys.argv) > 1:
    add(list_obj, sys.argv[1:])

save_to_json_file(list_obj, filename)

