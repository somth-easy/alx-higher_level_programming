#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Defines a class called square

        Attributes:
            size (DataFrame): private attribute of class Square
    """

    def __init__(self, size: int = 0):
        """Initialises the Square class

            args:
                size (DataFrame): value of size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        val = self.__size * self.__size
        return val
