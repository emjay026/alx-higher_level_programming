#!/usr/bin/python3
"""
Square - an empty class Square that defines a square.
"""


class Square:
    """Square - an empty class Square that defines a square."""

    def __init__(self, size=0):
        """Square - an empty class Square that defines a square.

        Args:
            size (int): the size of the square."""
        self.size = size

    def area(self):
        """Calculates the area of a square.

        Returns:
            the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Gets size of square.

        Returns:
            the current square area."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square

        Args:
            size (int): the size of the square."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Defines Square to be == comparable.

        Args:
            other (Square): other square object."""
        return self.area() == other.area()

    def __lt__(self, other):
        """Defines Square to be < comparable.

        Args:
            other (Square): other square object."""
        return self.area() < other.area()

    def __gt__(self, other):
        """Defines Square to be > comparable.

        Args:
            other (Square): other square object."""
        return self.area() > other.area()

    def __le__(self, other):
        """Defines Square to be <= comparable.

        Args:
            other (Square): other square object."""
        return self.area() <= other.area()

    def __ge__(self, other):
        """Defines Square to be >= comparable.

        Args:
            other (Square): other square object."""
        return self.area() >= other.area()
