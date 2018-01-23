#!/usr/bin/env python

def calculate():
    """
    Fibonacci generator
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

total = 0
for fib_number in calculate():
    if fib_number > 4000000:
        break
    print(fib_number)
    if fib_number % 2 == 0:
        total += fib_number

print("Total = {}".format(total))
