#!/usr/bin/python3
""" A function that returns true if the object
is an instance of a class that inherited
from the specified class """


def inherits_from(obj, a_class):
    """ Returns True if object is an instance of a_class
    that inherited from it
    Args:
        obj: the object to be checed
        a_class: the class to be checked against
    Returns:
        True if object is an instance of a_class,
        otherwise false
    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
