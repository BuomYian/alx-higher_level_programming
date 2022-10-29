#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """This represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initialises this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is < 0
        """

        self.width = width
        self.height = height

    @property	
    def width(self):
        """retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """retrieve height attrbute"""
        return self.__height


    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

	
    def area(self):
        """returns rectangle area"""
        return (self.__width * self.__height)


    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width *2) + (self.__height * 2))
