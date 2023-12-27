
#!/usr/bin/python3
""" A class called Base Geometry"""


class BaseGeometry:
    """ An empty class"""

    # Define an empty __getstate__ method to trigger its inclusion in dir()
    def __getstate__(self):
        pass


if __name__ == "__main__":
    BaseGeometry()
