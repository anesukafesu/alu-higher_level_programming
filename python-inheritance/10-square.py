#!/usr/bin/python3
"""
Implements a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator(self.size, 'size')
        self.__width = size
        self.__height = size
