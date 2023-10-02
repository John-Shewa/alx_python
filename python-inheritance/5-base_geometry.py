#!/usr/bin/python3
""" A class called Base Geometry"""


class BaseGeometry:
    """ An class with a public instance method
    def area(self)"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates if a value is an integer greater 
        than zero
        Args:
            name: neme of the value
            Value: value to be validated
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
