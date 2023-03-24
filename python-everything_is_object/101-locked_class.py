#!/usr/bin/python3
"""
Implements a locked class
Classes:
    - LockedClass
"""

class LockedClass:
    """
    Locked class that only allows you to set the first_name attribute
    """
    def __setattr__(self, key, value):
        if key == "first_name":
            self[key] = value
