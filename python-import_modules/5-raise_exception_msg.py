#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        message
    except NameError:
        print(f"{message}")
