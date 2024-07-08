#!/usr/bin/python3
""" Defines a Rectangle"""


class Rectangle:
    def __init__(self, width: int = 0, height: int = 0):
        """Initializes a new Rectangle instance

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for attribute width"""
        return self.__width

    @property
    def height(self):
        """getter for attribute height"""
        return self.__height

    @width.setter
    def width(self, value: int = 0):
        """setter for attribute width

        Args:
            value (int): value of width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is an int but less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value: int = 0):
        """setter for attribute height

        Args:
            value (int): value of height

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is an int but less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
