#!/usr/bin/python3
""" Module contains BaseGeometry Class.
    and Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class implements a Square"""

    def __init__(self, size):
        """ Initializes Square instance.

        Params:
            size (int): the size"""
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Function that calculates an area
            of geometrical shapes."""
        return self.__size * self.__size

    def print(self):
        """ Prints the Square."""
        print(f"[Square] {self.__size}/{self.__size}")

    def __str__(self):
        """ Returns the Square."""
        return (f"[Square] {self.__size}/{self.__size}")
