#!/usr/bin/python3

argument = input()
arg_list = argument.split()
lst_len = len(arg_list)
if lst_len == 0:
    print("{} arguments.".format(lst_len))
elif lst_len == 1:
    print("{} argument.".format(lst_len))
else:
    print("{} arguments:".format(lst_len))
for i in range(lst_len):
    print("{}: {}".format(i+1, arg_list[i]))
