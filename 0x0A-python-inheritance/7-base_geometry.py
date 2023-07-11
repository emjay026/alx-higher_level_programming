#!/usr/bin/python3
""" Module contains BaseGeometry Class."""


class BaseGeometry:
    """ This class implements base geometry."""

    def area(self):
        """ Function that calculates an area
            of geometrical shapes."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
