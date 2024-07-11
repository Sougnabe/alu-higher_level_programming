#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle with his characteristics"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0, number_of_instances=0):
        """
        init methode
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area getter """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = "\n".join(
                [str(self.print_symbol) *
                    self.__width for _ in range(self.__height)]
                )
        return rect

    def __repr__(self):
        """Return a string representation of
        the rectangle to recreate a new instance using eval.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """message after deleting a instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2     
    @classmethod
    def square(cls, size=0):
        """
        Return a new Rectangle instance with width == height == size.
        """
        return cls(size, size)
