#!/usr/bin/python3
"""It inherits from class BaseGeo"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
        width and height are private instances
    """
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
