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

    def to_json(self, attrs=None):
        """ Retrieves dictionary representation
            of an object.

            Params:
                attrs (list): list of strings

            Return:
                dictionary representation of this instance."""

        if type(attrs) == list and attrs is not None:
            result = {}
            for item in attrs:
                if item in self.__dict__:
                    result[item] = self.__dict__[item]
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces attributes of this object.

            Params:
                json (dict): a dictionary of attributes."""
        self.__dict__.update(json)
