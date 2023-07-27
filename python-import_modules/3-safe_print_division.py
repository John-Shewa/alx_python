#!/usr/bin/python3
def safe_print_division(a, b):
    """prints the result of division of 2 integers"""
    result = 0
    try:
        result = a / b        
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
