#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for integer in row:
            print("{integer:3d}".format(integer=integer), end=" ")
        print()