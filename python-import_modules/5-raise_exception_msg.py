#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise_exception_msg
    except NameError:
        print(f"{message}")     