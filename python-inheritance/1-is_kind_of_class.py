#!/usr/bin/python3
""" A function that returns true if object is
an instance of the class it inherited from
otherwise returns false"""


def is_kind_of_class(obj, a_class):
    """ Returns true if object is
    an instance of the class it inherited from
    otherwise returns false
    Args:
        obj: object to be checked
        a_class: class to check against
    Returns:
        True if object is an instance or false if it is not
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)


if __name__ == "__main__":
    is_kind_of_class
