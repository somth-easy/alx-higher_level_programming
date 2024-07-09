#!/usr/bin/python3
""" Defines a Rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """Initializes a new Rectangle instance

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """getter for attribute width"""
        return self.__width

    @property
    def height(self) -> int:
        """getter for attribute height"""
        return self.__height

    @width.setter
    def width(self, value: int) -> None:
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
    def height(self, value: int) -> None:
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

    def area(self) -> int:
        """calculates areaa of the rectangle"""
        return self.width * self.height

    def perimeter(self) -> int:
        """calculates the perimeter of the rectangle"""
        if (self.height == 0 or self.width == 0):
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self) -> str:
        """Return a string representation of the rectangle using # symbol"""
        if not (self.width == 0 or self.height == 0):
            return "\n".join(["#" * self.width for _ in range(self.height)])
        return ""

    def __repr__(self) -> str:
        """Returns a string representation of the created instance rectangle"""
        return f"{self.__class__.__name__}({self.width}, {self.height})"
