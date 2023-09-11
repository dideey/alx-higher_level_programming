#!/usr/bin/python3
"""a class with an area method"""


class BaseGeometry:
    """defining the method
        Raises:
            custom error
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the input value
            Raises:
                ValuEerror
                TypeError
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name}must be greater than 0")
