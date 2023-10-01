#!/usr/bin/python3

def is_prime(number):
    if number%1 == 0 and number%number == 0:
        return True;
    else:
        return False;