#!/usr/bin/python3
""" A class called Square that inherits from 
the class BaseGeometry defined in 7-base_geometry.py"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """ A class that defines a square"""

    def __init__(self, size):
        """ initialization of square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculates the area of a square
        Returns:
            Area of square
        """
        return self.__size ** 2
