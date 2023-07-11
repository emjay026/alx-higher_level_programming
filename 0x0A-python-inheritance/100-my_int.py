#!/usr/bin/python3
""" Module contains MyInt Class.
    that wraps the int object."""

class MyInt(int):

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
