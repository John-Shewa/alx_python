#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for integer in row:
            print("{:3d}".format(integer), end=" ")
        print()