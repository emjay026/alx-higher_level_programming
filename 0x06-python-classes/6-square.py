#!/usr/bin/python3
"""
Square - an empty class Square that defines a square.
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """initializes a square.

        Args:
            size (int): the size of the square.
            position (tuple): a position in a square"""
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of a square.

        Returns:
            the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints a square using the # character"""
        if self.__size == 0:
            print("")
        else:
            for g in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for h in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def size(self):
        """Gets size of square.

        Returns:
            the size of a square."""
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

    @property
    def position(self):
        """Gets the position in the square.

        Returns:
            position in the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets position value

        Args:
            value (tuple): 2d position in a square."""
        error = "position must be a tuple of 2 positive integers"
        if type(value) == tuple and len(value) != 2:
            raise TypeError(error)
        x, y = value
        if type(x) != int or type(y) != int:
            raise TypeError(error)
        if x < 0 or y < 0:
            raise TypeError(error)
        self.__position = value
