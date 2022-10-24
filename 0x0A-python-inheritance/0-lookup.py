#!/usr/bin/python3
"""

This module has a function that returns a list

"""
def lookup(obj):
    """Function that returns the list of available attributes and method of an object

    Args:
        obj: arguments of list
    """
    return ([x for x in dir(obj)])
