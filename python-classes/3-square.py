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
        self._size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """The property of size."""
        return self._size

    @size.setter
    def size(self, new_size):
        """A setter for value"""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        self._size = new_size

    def area(self):
        """ 
        Args:
            self.__size: size of the square.
        Returns:
            The area of the square.
        """
        return (self._size * self._size)
