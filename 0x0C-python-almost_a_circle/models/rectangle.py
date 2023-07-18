#!/usr/bin/python3
""" This module implements the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """ The Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes an instance of Rectangle.

            Params:
                __width (int): the width of a rectangle
                __height (int): the height of a rectangle
                __x (int): the x coordinate
                __y (int): the y coordinate"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculates an Area of a Rectangle.

            Return:
                area (int)"""
        return self.__width * self.__height

    def display(self):
        """ Prints a rectangle"""
        # str = ""
        # if self.__width == 0 or self.__height == 0:
        #     return str
        # else:
        #     for i in range(self.__height):
        #         for j in range(self.__width):
        #             str += "#"
        #         if i < self.__height - 1:
        #             str += "\n"
        # print(str)

        """Prints a square using the # character"""
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            for g in range(self.__y):
                print("")
            for i in range(self.__height):
                for h in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print("")

    def __str__(self):
        """ Prints a rectangle"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f"- {self.__width}/{self.__height}")
