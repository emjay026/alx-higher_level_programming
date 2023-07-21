#!/usr/bin/python3
""" This module describes a Class that defines a Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class that defines a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a square

        Args:
            size (int): the size of the square.
            position (tuple): a position in a square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints Square"""
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")

    @property
    def size(self):
        """ Getter for width."""
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for width and height."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates this Square's attributes

            args (tuple): accepts multiple values.
            kwargs (dictionary): acceps multiple keyworded values."""
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
