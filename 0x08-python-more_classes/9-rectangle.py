#!/usr/bin/python3
"""
Defining my class Rectangle
"""


class Rectangle:
    """Representing my rectangle."""
    print_symbol = '#'

    def __init__(self, width=0, height=0, number_of_instances=0):
        """Initializing a new Rectangle.
        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        self.width = width
        self.height = height
        self.number_of_instances += number_of_instances
        self.print_symbol = print_symbol

    def __str__(self):
        """Getting the width of the Rectangle."""
        return self.print_symbol

    @property
    def width(self):
        """setting the height of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perim = (self.__height + self.__width)*2
        if (self.__width == 0 or self.__height == 0):
            perim = 0
        return perim

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        rectang = ''
        for i in range(self.__height):
            rectang += '#' * self.__width
            if i != self.__height - 1:
                rectang += '\n'
        return rectang

    def __repr__(self):
        return eval((f"Rectangle({self.width}, {self.height})"))

    def __del__(self):
        self.number_of_instances += number_of_instances
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1 is not isinstance(Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 > rect_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        self.width = size
        self.height = size
