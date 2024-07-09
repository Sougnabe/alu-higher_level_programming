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
        the size setter
        """
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
    @property
    def position(self):
        return self.__position
    @position.settter
    def position(self, value=(0, 0)):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
