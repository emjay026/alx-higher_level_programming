#!/usr/bin/python3
""" This module implements the Base Class."""


class Base:
    """ Base - The Super Class of a Package.

        Class Attributes:
            __nb_objects (int): holds number of Base objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializer of Base instances.

            Params:
                id (int): instance tracking number"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
