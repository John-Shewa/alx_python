#!/usr/bin/python3
""" A function that returns true if the object is an instance of a class that inherited
from the specified class """


def inherits_from(obj, a_class):
    """ Initializes an object to check for inheritance
            Args:
            obj: the object to be checked
            a_class: the class to be checked against
            checks if object inherits from the specified class.
            Returns:
            True if object is an instance of a_class, otherwise false
    """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
