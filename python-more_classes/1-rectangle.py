#!/usr/bin/python3
"""This module implements a Rectangle"""


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
        if not isinstance(dimension, int):
            raise TypeError('f{dimension} must be an integer')
        
        if value < 0:
            raise TypeError('f{dimension} must be >= 0')

        if dimension == 'width':
            self.__width = value
        else:
            self.__height = value

    @property
    """ The width of the rectangle (int)
    """
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__set_dimension('width', value)

    @property
    """ The height of the rectangle (int)
    """
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__set_dimension('height', value)

    def __init__(self, width=0, height=0):
        self.__set_dimension('width', width)
        self.__set_dimension('height', height)
