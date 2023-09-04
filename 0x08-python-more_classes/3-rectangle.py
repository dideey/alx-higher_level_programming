#!/usr/bin/python3
"""
Defining my class Rectangle
"""


class Rectangle:
    """Representing my rectangle."""
    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.
        Args:
            width (int): new rectangle width.
            height (int): new rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter of the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter of the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area"""
        area = (self.__width * self.__height)
        return area

    def perimeter(self):
        """return perimeter"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """printing"""
    if self.__width == 0 or self.__height == 0:
        return ""
    else:
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str
