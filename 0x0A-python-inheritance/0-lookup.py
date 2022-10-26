#!/usr/bin/pythton3
"""
    This module returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """This function looks out for all attributes and method of an object"""
    return ([x for x in dir(obj)])
