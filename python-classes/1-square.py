#!/usr/bin/python3
class Square:
    """ 
    This is a class that defines a square. 

    """

    def __init__(self, size=0):
        """
        Args:
            size: the size of the square

        Returns:
            the size of a square

        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
