#!/usr/bin/python3
"""initilaizing a private atribute to
the square class and must be an integer"""


class Square:
    """class"""
    def __init__(self, size=0):
        """mesthod where i initialize the size field.
        Args:
            size
        Raises:
            Typeerror if not int
            Valueerror if less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """"returns area"""
        return size * size
