#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    key = str(key)
    updated_dict = {}
    for element in a_dictionary:
        if key in a_dictionary:
            updated_dict(a_dictionary, value)
        else:
            updated_dict(a_dictionary, key, value)
    return updated_dict
