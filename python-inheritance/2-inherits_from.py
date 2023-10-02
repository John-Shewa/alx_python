#!/usr/bin/python3
""" A function that returns true if the object
is an instance of a class that inherited
from the specified class"""


def inherits_from(obj, a_class):
    """ Returns True if object is an instance of a_class
    that inherited from it
    Args:
        obj: the object to be checed
        a_class: the class to be checked against
    Returns:
        True if object is an instance of a_class
    """
    if isinstance(obj, a_class):
        return True

    for parent in type(obj).__bases__:
        if inherits_from(parent, a_class):
            return True
    return False
