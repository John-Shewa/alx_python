#!/usr/bin/python3
""" A function that returns true if the object
is an instance of a class that inherited
from the specified class """


class inherits_from:
    def __init__(self, obj, a_class):
        self.obj = obj
        self.a_class = a_class

    def inherits_from(obj, a_class):
        """ Returns True if object is an instance of a_class
            that inherited from it
            Args:
            obj: the object to be checked
            a_class: the class to be checked against
            Returns:
            True if object is an instance of a_class,
            otherwise false
        """

        return (issubclass(type(obj), a_class) and type(obj) != a_class)
