#!/usr/bin/python3
""" Module contains BaseGeometry Class.
    and Rectangle."""


class BaseGeometry:
    """ This class implements base geometry."""

    def __init__(self):
        """ Initializes BaseGeometry instance"""
        pass

    def area(self):
        """ Function that calculates an area
            of geometrical shapes."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Function that validates integers
            used by this class.

            Params:
                name (str): string name
                value (int): value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ his class implements a rectangle"""

    def __init__(self, width, height):
        """ Initializes Rectangle instance."""
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
