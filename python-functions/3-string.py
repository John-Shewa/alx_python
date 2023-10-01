#!/usr/bin/python3

def reverse_string(string):
    reverse_string = ""
    for i in range(len(string) -1, -1, -1):
        reverse_string += string[i]
    return reverse_string
