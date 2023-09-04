#!/usr/bin/python3
"""A class with private
    getters and setters
"""


class Rectangle:

    def __init__(self, width=0, height=0)
    self._width = width
    self._height = height


""" Method declaring the width and height
"""


@property
def width(self):
    return self._width


"""private getter for width
"""


@width.setter
def width(self, value):
    if value is not int
    raise TypeError("width must be an integer")
    elif value < 0
    raise ValueError("width must be >= 0")
    else
    self._width = value


"""private setter for width
"""


@property
def height(self):
    return self._height


"""private getter for height
"""


@height.setter
def height(self, value):
    if value is not int
    raise TypeError("height must be an integer")
    elif value < 0
    raise ValueError("height must be >= 0")
    else
    self._height = value


"""Private setter for height
"""
