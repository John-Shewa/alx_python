#!/usr/bin/python3

def fibonacci_sequence(n):
    if n < 0:
        return[]
    if n == 0 or n == 1:
        return[0] * n
    
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i -2])
    return(fib_sequence)