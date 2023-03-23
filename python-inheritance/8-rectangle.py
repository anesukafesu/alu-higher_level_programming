#!/usr/bin/python3
"""
Implements BaseGeometry class
Classes:
    - BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        if type(name) != str:
            raise TypeError(f'{name} must be an integer')

        if value < 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)

        self.__width = width
        self.__height = height
    
    def area():
        return self.__width * self.__height

    def __str__():
        return f'[Reactangle] {self.__width}/{self.__height}'
