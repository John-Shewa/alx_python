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
        self.size = size

        @property
        
        def size(self):
            """The property of size."""
            return self.__size
        
        @size.setter
        def size(self, size):
            """A setter for value"""
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        """ 
        Args:
            self.__size: size of the square.
        Returns:
            The area of the square.
        """
        return (self.size * self.size)
