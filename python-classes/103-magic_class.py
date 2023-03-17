#!/usr/bin/python3
"""
Implements a circle
I am doing this exercise at 2 3.14hrs
"""

import math

class MagicClass:
    """
    This is a magic class
    """
    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        
        self.radius = radius

    def area():
        return math.pi * radius ** 2

    def circumference():
        return math.pi * radius * 2
