#!/usr/bin/python3

def no_c(my_string):
    created_string = ""
    for char in my_string:
        if char != "c" and char != "C":
            created_string += char
    return created_string