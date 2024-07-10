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
        self.__position = position

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

    @property
    def position(self):
        """
        getter of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter of position
        """
        if (
            type(value) is not tuple or
                len(value) != 2 or not
                all(isinstance(num, int) for num in value)or not
                all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Prints in stdout the square with the character #
        If size is equal to 0, prints an empty line

        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

if __name__ == "__main__":
    Square = __import__("6-square").Square

    my_square_1 = Square(5, (3, 2))
    my_square_1.my_print()

    print("--")
