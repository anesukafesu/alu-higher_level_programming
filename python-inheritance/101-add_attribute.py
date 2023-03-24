#!/usr/bin/python3
"""
Gently adds attributes
"""


def add_attribute(obj, name, value):
    """
    Consent culture
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
