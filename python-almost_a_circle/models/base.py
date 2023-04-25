#!/usr/bin/python3
"""
Implements the base model
"""

class Base:
    """
    Base class
    """
    __nb_objects = 0

    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
