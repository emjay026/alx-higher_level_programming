#!/usr/bin/python3
"""This module implements a class that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object

        Parameters:
            width (int): the width of the rectangle
            height (int): the height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width of rectangle.

        Returns:
            the width of a rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value

        Parameter:
            value (int): width of rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height of rectangle.

        Returns:
            the height of a rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value

        Parameter:
            value (int): height of rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of rectangle

        Returns:
            the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter a of rectangle

        Returns:
            the perimeter a of rectangle"""
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (2 * (self.__width + self.__height))
        return perimeter

    def __str__(self):
        """Prints a rectangle"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    str += "#"
                if i < self.__height - 1:
                    str += "\n"
        return str
