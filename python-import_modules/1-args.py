#!/usr/bin/python3
if __name__ == '__main__':
    """print number of arguments"""

    import sys

    arg_len = len(sys.argv) - 1
    if arg_len == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_len))
    for i in range(arg_len):
        print("{}: {}".format(i+1, syst.argv[i+1]))
