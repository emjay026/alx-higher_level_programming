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
        """int: stores the size of the attribute"""

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
        """Sets size value

        Args:
            size (int): the size of the square."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square using the # character"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
