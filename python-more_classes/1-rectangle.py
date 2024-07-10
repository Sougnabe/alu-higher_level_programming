#!/usr/bin/python3
""" no module importation"""


class Rectangle():
    """
    a rectangle has four sides
    """
    def __init__(self, width=0, height=0):
        """ init module """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        "width gettere"
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        "height getter"
        return self.__heigth
    
    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int): 
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
