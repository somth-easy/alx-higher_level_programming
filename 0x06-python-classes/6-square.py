#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Defines a class called Square.

    Attributes:
        size (int): Private attribute of class Square.
        position (tuple): The position of the Square.
    """

    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """Initializes a new Square.

        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Getter for position attribute."""
        return self.__position

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for size attribute with validation.

        Args:
            size (int): Value to set the size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, position):
        """Setter for position attribute.

        Args:
            position (tuple): Value to set the position.

        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(num, int) for num in position) or \
           not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: Area of the Square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using # character.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print(' ' * self.position[0] + '#' * self.size)

