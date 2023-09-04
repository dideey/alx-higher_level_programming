#!/usr/bin/python3
"""a class Rectangle that defines a rectangle

    Raises:
        TypeError: the rectangle width must be an integer
        ValueError: the rectangle width must be greater or == 0
        TypeError: the rectangle height must be an integer
        ValueError: the rectangle height must be >= 0

    Returns:
        int: Rectangle height
"""


class Rectangle:
    """a class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """initialization  of private instances

        Args:
            width (int, optional): Rectangles width. Defaults to 0.
            height (int, optional): Rectangles height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getting the with property of the rectangle class

        Returns:
            int: Rectangle width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setting the rectangle width

        Args:
            value (int): value to be passed from the instance of rectangle

        Raises:
            TypeError: the passed value must be an integer
            ValueError: the passed value must not be a negative value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting the height property of the rectangle class

        Returns:
            int: Rectangle height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setting the rectangle width

        Args:
            value (int): value to pe passed from the instance of rectangle

        Raises:
            TypeError: the passed value must be an integer
            ValueError: the passed value must not be a negative value
        """
        if not isinstance(value, int):
            raise TypeError("height  must be an integer")
        if value < 0:
            raise ValueError("height  must be >= 0")
        self.__height = value
