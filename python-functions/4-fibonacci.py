#!/usr/bin/python3

def fibonacci_sequence(n):
    if n < 0:
        return[]
    fib_seqence = [0, 1]
    for i in range(2, n+1):
        fib_seqence.append(fib_seqence[i - 1] + fib_seqence[i -2])
    return(fib_seqence)