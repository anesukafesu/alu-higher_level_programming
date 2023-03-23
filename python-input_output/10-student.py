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

    def to_json(self, attributes=None):
        """
        Returns a JSON-friendly object that represents the instance
        Args:
            - attributes @optional (list) - the attributes to return
            if unspecified everything is returned
        """
        # Stores all attributes before filtering
        preliminary_result = {}

        # Stores the filtered attributes
        result = {}

        # Get class attributes
        # For this class there are no class attributes
        # But in the event that they are added in future
        # This method will still work
        for key, value in self.__class__.__dict__.items():
            if not (key[:2] == "__" or callable(value)):
                preliminary_result[key] = value

        # Get instance attributes
        for key, value in self.__dict__.items():
            preliminary_result[key] = value

        # Filter for attrs
        if attributes is None:
            result = preliminary_result
        else:
            for attribute in attributes:
                # Adding to the result if the attribute exists
                if attribute in preliminary_result:
                    result[attribute] = preliminary_result[attribute]

        return result
