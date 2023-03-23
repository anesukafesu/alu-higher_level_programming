#!/usr/bin/python3
"""
Implements the class_to_json method
"""

def class_to_json(obj):
    """
    Converts any object of any class to a json-serialisable object
    Args:
        - obj (object) - The object to simplify
    Returns:
        - obj (object) - The simplified object
    """
    result = {}

    # Get all class attributes
    for key, value in obj.__class__.__dict__.items():
        
        # Filtering default class attributes and functions
        if key[:2] != "__" and not callable(value):
            result[key] = value

    # Get all instance attributes
    # Setting instance attributes after class attributes
    # So that instance attributes override class attributes
    for key, value in obj.__dict__.items():
        result[key] = value

    return result
