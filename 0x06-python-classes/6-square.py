#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Defines a class called square

        Attributes:
            size (DataFrame): private attribute of class Square
    """

    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """Initialises the Square class

            Args:
                size (DataFrame): value of size
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

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

    @position.setter
    def position(self, position):
        """ Setter for position attribute

        Args:
            position (tuple): value to set the position

        Raises:
            TypeError: if position is not a tuple of two positive ints
        """
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive intefers")
        self.__position = position

    def area(self):
        """Calculates the area of the square

        Returns:
            val (int): area of the Square
        """
        val = self.__size * self.__size
        return val

    def my_print(self):
        """Prints the square using # character
        
        if size is equal to 0, prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print(' ' * self.position[0] + '#' * self.size)
