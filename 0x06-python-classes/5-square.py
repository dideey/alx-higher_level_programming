#!/usr/bin/python3
"""initilaizing a private atribute to
the square class and must be an integer"""


class Square:
    """class"""
    def __init__(self, size=0):
        """method where i initialize the size field.
        """
        self.__size = size

    @property
    def size(self):
        """property setter to retrieve the size attribute

        Returns:
            int: returns the Square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter

        Args:
            value (int): private instance attribute

        Raises:
            TypeError: size must be an integer
            ValueError: if size is less than 0,
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """"returns area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square to std
        output
        """
        if self.__size == 0:
        print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
