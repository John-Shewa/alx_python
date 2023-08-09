#!/usr/bin/python3

"""This module defines a class called Square.

A Square object has a size attribute that represents its side length.

The Square class has one method:

    * __init__(self, size): This method initializes the Square object with the given size.

"""


class Square:
    """ This is a class that represents a square."""

    def __init__(self, size):
        """ Initializes the Square object with the given size."""
        self.__size = size
