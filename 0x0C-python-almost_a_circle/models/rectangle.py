#!/usr/bin/python3

"""ïmporting the base class"""
from models.base import Base


class Rectangle(Base):
    """
    class rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """seting the values"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    """
    getter
    """
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):

        iid = "({})".format(self.id)
        xy = " {}/{} - ".format(self.__x, self.__y)
        widhe = "{}/{}".format(self.__width, self.__height)
        return "[Rectangle] " + iid + xy + widhe

    def update(self, *args, **kwargs):
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y,
                }
