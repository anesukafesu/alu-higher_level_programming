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
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return math.pi * self.radius * 2
