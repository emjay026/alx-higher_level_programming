#!/usr/bin/python3
""" Module contains BaseGeometry Class.
    and Rectangle."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class implements a rectangle"""

    def __init__(self, width, height):
        """ Initializes Rectangle instance.

        Params:
            width (int): the width
            height (int): the hight"""
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Function that calculates an area
            of geometrical shapes."""
        return self.__width * self.__height

    def print(self):
        """ Prints the Rectangle."""
        print(f"[Rectangle] {self.__width}/{self.__height}")

    def __str__(self):
        """ Returns the Rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
