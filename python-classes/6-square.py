#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): Size of the square.
            position (tuple): Position offset (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (
            type(value) is not tuple or
            len(value) != 2 or
            type(value[0]) is not int or
            type(value[1]) is not int or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using # with position offsets."""
        if self.__size == 0:
            print("")
            return

        # vertical offset (position[1])
        for _ in range(self.__position[1]):
            print("")

        # print square lines with horizontal offset (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
