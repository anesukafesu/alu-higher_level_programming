#!/usr/bin/python3
"""This module gives us a Rectangle"""


class Rectangle:
    """Rectangle class"""
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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """The width of the rectangle"""
        self.__set_dimension('width', value)

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__set_dimension('height', value)

    def __init__(self, width=0, height=0):
        self.__set_dimension('width', width)
        self.__set_dimension('height', height)
