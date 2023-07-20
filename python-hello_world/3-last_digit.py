#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
edited_number = str(number)
new_number = edited_number[-1]
string_number = int(new_number)
if string_number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, string_number))
elif string_number == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, string_number))
elif string_number < 6 and string_number != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, string_number))
