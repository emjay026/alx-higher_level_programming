#!/usr/bin/python3
"""This module implements a class that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle

    Attributes:
        number_of_instance (int): tracks number of rectangle instances
        print_symbol (char): symbol for string representation"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object

        Parameters:
            width (int): the width of the rectangle
            height (int): the height of the rectangle"""
        self.width = width
        self.height = height
        Rectangle.increment_rectangle()

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
        str_ = ""
        if self.__width == 0 or self.__height == 0:
            return str_
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    str_ += str(self.print_symbol)
                if i < self.__height - 1:
                    str_ += "\n"
        return str_

    def __repr__(self):
        """Prints a rectangle representation"""
        str_ = ""
        if self.__width == 0 or self.__height == 0:
            return str_
        else:
            str_ += "Rectangle"
            str_ += "("
            str_ += "{:d}".format(self.__width)
            str_ += ", "
            str_ += "{:d}".format(self.__height)
            str_ += ")"
        return str_

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.decrement_rectangle()

    @classmethod
    def increment_rectangle(cls):
        cls.number_of_instances += 1

    @classmethod
    def decrement_rectangle(cls):
        cls.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
