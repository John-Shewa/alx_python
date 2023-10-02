#!/usr/bin/python3
""" A class called rectangle that inherits from 
the class BaseGeometry defined in 5-base_geometry.py"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class that defines a rectangle"""

    def __init__(self, width, height):
        """ initialization of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height


if __name__ == '__main__':
    Rectangle()
