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
