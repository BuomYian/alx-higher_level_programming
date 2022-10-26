#!/usr/bin/python3
"""
Define a base geometry class from BaseGeometry
"""


class BaseGeometry:
    """This class represents a base geometry"""

    def area(self):
        """Public instance method that raises an exception with the message"""
        raise Exception("area() is not implemented")
