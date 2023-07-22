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
        """ Prints a rectangle using the # character"""
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
                f" - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ Updates this Rectangle's attributes

            args (tuple): accepts multiple values.
            kwargs (dictionary): acceps multiple keyworded values."""
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ Returns a list of attributes

            Return:
                list."""
        dic = {}
        dic['id'] = self.id
        dic['width'] = self.width
        dic['height'] = self.height
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
