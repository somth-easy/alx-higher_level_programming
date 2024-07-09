#!/usr/bin/python3
""" Defines a Rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(
            self, width: int = 0, height: int = 0,
                ) -> None:
        """Initializes a new Rectangle instance

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = "#"

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

    @classmethod
    def number_of_instance(cls) -> int:
        """Returns the nr of rectangles created"""
        return cls.number_of_instances

    @staticmethod
    def bigger_or_equal(
            rect_1: 'Rectangle', rect_2: 'Rectangle'
            ) -> 'Rectangle':
        """Returns the bigger rectangle or rect1 if they equal

        Args:
            rect1 (Rectangle): 1st rectangle to compare.
            rect2 (Rectangle): 2nd rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger area or
            the first rectangle if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size: int = 0) -> 'Rectangle':
        """Creates a new instance of rectangle.

        Args:
            size (int): value to be assigned new isntance parameters

        Returns:
            Rectangle: a new instance
        """
        new_instance = Rectangle(size, size)
        return new_instance

    def __str__(self) -> str:
        """Return a string representation of the rectangle using # symbol"""
        if not (self.width == 0 or self.height == 0):
            return "\n".join(
                [str(self.print_symbol) * self.width
                 for _ in range(self.height)]
            )
        return ""

    def __repr__(self) -> str:
        """Returns a string representation of the created instance rectangle"""
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self) -> None:
        """Returns a string when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
