#!/usr/bin/python3
def safe_print_integer(value):
    success = True
    try:
        print("{:d}".format(value))
        success = True
    except ValueError:
        success = False
    return success
