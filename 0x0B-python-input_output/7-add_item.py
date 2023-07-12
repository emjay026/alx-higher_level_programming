#!/usr/bin/python3
""" Reads in arguments from the command line
    and saves then to a .json file."""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"


def load_obj(filename):
    """ loads json from file
        or creates json file if DNE."""
    result = ""
    try:
        result = load_from_json_file(filename)
    except FileNotFoundError:
        save_to_json_file([], filename)
    return result


list_obj = load_obj(filename)

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        list_obj.append(arg)
    save_to_json_file(list_obj, filename)
