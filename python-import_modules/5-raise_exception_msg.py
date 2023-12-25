#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise_exception_msg
        print(f"{message}")
    except NameError as ne:
        print(ne)
