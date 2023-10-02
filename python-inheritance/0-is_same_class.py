#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ A function that returns True if the object is 
    an instance of the class
    Args: 
        obj: object to be checked
        a_class: class to check against
    """
    return type(obj) == a_class
