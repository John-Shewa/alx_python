#!/usr/bin/python3
def raise_exception():
    add = "1"
    try:
        add = add / 2
    except TypeError:
        print("Exception raised")
    finally:
        return add

if __name__ == '__main__':
    raise_exception()

