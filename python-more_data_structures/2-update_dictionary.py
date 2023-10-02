#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    if not isinstance(key, str):
        raise TypeError("key must be a string")
    a_dictionary[key] = value
