#!/usr/bin/python3
""" This module defines a class called Rectangle which inherits from the class called Base in the models folder"""
from models.base import Base


class Rectangle(Base):
    """ This is a class called Rectangle"""
    __width = 0

    @property
    def width(self):
        """ The property of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ A setter of width"""
        self.__width = width

    __height = 0

    @property
    def height(self):
        """ The property of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """ A setter of height"""
        self.__height = height

    __x = 0

    @property
    def x(self):
        """ The property of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """ A setter of x"""
        self.__x = x

    __y = 0

    @property
    def y(self):
        """ The property of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """ A setter of y"""
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This calls the __init__() constructor of the Base class with id argument"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
