#!/usr/bin/python3

"""
This following classe is empty
"""


class Square():
    """
    This class doesn't have modules
    """
    def __init__(self, size=0):
        """
        Now the class has a module
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        give the erea of teh current square
        """
        return self.__size**2

    @property
    def size(self):
        """
        the size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        the setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        self.__size = value
