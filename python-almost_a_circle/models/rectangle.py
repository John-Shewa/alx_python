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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    __height = 0

    @property
    def height(self):
        """ The property of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """ A setter of height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    __x = 0

    @property
    def x(self):
        """ The property of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """ A setter of x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    __y = 0

    @property
    def y(self):
        """ The property of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """ A setter of y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This calls the __init__() constructor of the Base class with id argument"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ This defines the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """ This prints the rectangle with '#' by taking care of x and y"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.width):
                if i < self.y or i >= self.y + self.height:
                    print(" ", end="")
                else:
                    if j < self.x or j >= self.x + self.width:
                        print("#", end="")
                    else:
                        print(" ", end="")
            print()

    def __str__(self):
        """ This returns a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
