#!/usr/bin/python3
"""This module contains the addition function"""

def add_integer(a, b=98):
    """Adds two integers

    Params:
        a (int): first number
        b (int): second number"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
