#!/usr/bin/python3
""" This module defines a class called Square which inherits from the class called Rectangle in the models folder"""
from models.rectangle import Rectangle

class Square:
    def __init__(self, size, x=0, y=0, id=None):
         super().__init__(id)
         self.width = size
         self.height = size
         self.x = x
         self.y = y

def __str__(self):
        """ This returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)