#!/usr/bin/env python

def calculate(up_to):
    print("Calculating up to {}".format(up_to))
    total = 0
    for i in range(1, up_to):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    return total

print("Total sum is {}".format(calculate(1000)))
