#!/usr/bin/python3
"""This module creates a rectangle

Classes:
    Rectangle
"""


class Rectangle:
    """A class to represent a person
    Attributes:
        height (int) The height of the rectangle
        width (int) The width of the rectangle
    Methods:
        height(value) Sets the height of the rectangle
        width(value) Sets the width of the rectangle
        area() Returns the area of the rectangle
        perimeter() Returns the perimeter of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __set_dimension(self, dimension, value):
        """
        Private instance method to set either the height or width
        Args:
            - dimension (str): Either 'width' or 'height'
            - value (int): Must be greater than zero
        Returns:
            - None
        """
        if not isinstance(value, int):
            raise TypeError(f'{dimension} must be an integer')

        if value < 0:
            raise ValueError(f'{dimension} must be >= 0')

        if dimension == 'width':
            self.__width = value
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        def raise_error(rect):
            raise TypeError(f'{rect} must be an instance of Rectangle')

        if not isinstance(rect_1, Rectangle):
            raise_error('rect_1')

        if not isinstance(rect_2, Rectangle):
            raise_error('rect_2')

        return rect_2 if rect_2.area() > rect_1.area() else rect_1

    @property
    def width(self):
        """ The width of the rectangle (int)"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__set_dimension('width', value)

    @property
    def height(self):
        """ The height of the rectangle (int)"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__set_dimension('height', value)

    def area(self):
        """The area"""
        return self.__height * self.__width

    def perimeter(self):
        """The perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        s = self.print_symbol
        return ((f'{s}' * self.__width + "\n") * self.__height).rstrip()

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print('Bye rectangle...')
        self.__class__.number_of_instances -= 1

    def __init__(self, width=0, height=0):
        self.__set_dimension('width', width)
        self.__set_dimension('height', height)
        self.__class__.number_of_instances += 1
