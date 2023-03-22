#!/usr/bin/python3
"""
Implements the is_same_class function which checks if an object is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of the specified class
    Args:
        - obj (Object) - The object to check
        - a_class(Class) - The class to compare with
    Returns:
        - Boolean - True if the object is an instance of the class and False if it is not
    """
    return isinstance(obj, a_class)
