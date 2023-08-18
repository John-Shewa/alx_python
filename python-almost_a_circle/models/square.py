#!/usr/bin/python3
""" This module defines a class called Square which inherits from the class called Rectangle in the models folder"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
         """ Initializes a square
         Args:
            size: size of square
            x: x coordinate of square
            y: y coordinate of square
            id: id of the square
         """
         super().__init__(size, size, x, y, id)

         @property
         def size(self):
               """ size of square"""
               return self.width
         @size.setter
         def size(self, value):
               self.width = value
               self.height = value
         
def __str__(self):
        """ This returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)