#!/usr/bin/python3
"""This module defines a class called Square.

A Square object has a size attribute that represents its side length.

The Square class has one method:

    * __init__(self, size): This method initializes the Square object with the given size.

"""


class Square:
    """ This is a class that defines a square."""

    def __init__(self, size=0):
        """ Initializes the Square object with the given size."""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (size * size)
