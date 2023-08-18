#!/usr/bin/python3
""" This module defines a class called Base
    The Base class has one method:
    __init__(self, id=None): This method initializes the Base object with the given id set to None.

"""


class Base:
    """ This is a class that represents Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the Base object with the given id"""
        self.id = id
    __nb_objects += 1
