#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Defines a class called square

        Attributes:
            size (DataFrame): private attribute of class Square
    """

    def __init__(self, size: int = 0):
        """Initialises the Square class

            Args:
                size (DataFrame): value of size
        """
        self.__size = size

    @property
    def size(self):
        """" Getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """ Setter for size attribute with validation

        Args:
            size (int): value to set the size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            val (int): area of the Square
        """
        val = self.__size * self.__size
        return val

    def my_print(self):
        """Prints the square using # character"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('{}'.format('#'*self.__size))
