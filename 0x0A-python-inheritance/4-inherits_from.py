#!/usr/bin/python3
"""
This module checks if the object is an instance of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """Returns True if the objects is an instance of a class that inherited from the specified class; Otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
