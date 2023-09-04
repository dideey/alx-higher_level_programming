#!/usr/bin/python3
"""a class Rectangle that defines a rectangle

    Raises:
        TypeError: the rectangle width must be an integer
        ValueError: the rectangle width must be greater or == 0
        TypeError: the rectangle height must be an integer
        ValueError: the rectangle height must be >= 0
        TypeError: ensuring that rect_1 is an instance of Rectangle class
        TypeError: ensuring that rect_2 is an instance of Rectangle class

    Returns:
        class: a new rectangle
"""


class Rectangle:
    """a class Rectangle that defines a rectangle

    Raises:
        TypeError: the rectangle width must be an integer
        ValueError: the rectangle width must be greater or == 0
        TypeError: the rectangle height must be an integer
        ValueError: the rectangle height must be >= 0
        TypeError: ensuring that rect_1 is an instance of Rectangle class
        TypeError: ensuring that rect_2 is an instance of Rectangle class

    Returns:
        class: a new rectangle
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area method of the Rectangle class which calculates
            the area of a Rectangle instance

        Returns:
            int: the total area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """method which calculates the perimeter of the Rectangle instance

        Returns:
            int: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """built-in python method to print string from an object instance

        Returns:
            str: rectangle in string format
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = str(self.print_symbol) * self.__width + "\n"
        shape *= self.__height
        return shape[:-1]

    def __repr__(self):
        """built-in python method that converts an object instance to int

        Returns:
            tuple: values of the Rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """built-in method that is used to check for deleted object instance
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method that checks if a rectangles width is more in
            length or the height is more

        Args:
            rect_1 (Rectangle): instance of the Rectangle class
            rect_2 (Rectangle): instance of the Rectangle class

        Raises:
            TypeError: rect_1 must be a valid type (instance of Rectangle)
            TypeError: rect_2 must be a valid type (instance of Rectangle)
        Returns:
            _type_: _description_
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """method that checks if an instance is a square

        Args:
            size (int, optional): size of the square that will be used for
                the check. Defaults to 0.

        Returns:
            Rectangle: a rectangle instance
        """
        return cls(size, size)
