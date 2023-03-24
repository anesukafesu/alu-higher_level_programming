#!/usr/bin/python3
"""
Gently adds attributes
"""

def add_attribute(obj, name, value):
    """
    Consent culture
    """
    if hasattr(obj, name):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
