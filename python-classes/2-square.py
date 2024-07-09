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
        self.__size = size
        if size is not int:
            raise TypeError"size must be an integer"
        elif size < 0:
            raise TypeError"size must be >= 0"
