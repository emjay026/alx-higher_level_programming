#!/usr/bin/python3
""" A Class that defines a Student."""


class Student:
    """ Defines a student."""

    def __init__(self, first_name, last_name, age):
        """ Initializes Student object

            Params:
                first_name (str): student first name
                last_name (str): student last name
                age (int): student age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves dictionary representation
            of an object."""
        return self.__dict__
