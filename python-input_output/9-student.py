#!/usr/bin/python3
"""
Implements the Student class
Classes:
    - Student
"""


class Student:
    """
    Student class
    Attributes:
        - first_name (str)
        - last_name (str)
        - age (int)
    Methods:
        - to_json
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a JSON-friendly object that represents the instance
        """
        result = {}

        # Get class attributes
        # For this class there are no class attributes
        # But in the event that they are added in future
        # This method will still work
        for key, value in self.__class__.__dict__.items():
            if not (key[:2] == "__" or callable(value)):
                result[key] = value

        # Get instance attributes
        for key, value in self.__dict__.items():
            result[key] = value

        return result
