#!/usr/bin/env python

def generate_prime(max_number):
    """
    Prime number generator
    """
    for i in range(max_number, 2, -1):
        # Is the number a prime?
        for factor in range(i-1, 2, -1):
            if i % factor == 0:
                break
        if factor == 2:
            yield i

def calculate_slow(number):
    """
    Find the prime factors of number
    Very slow!
    """
    for prime in generate_prime(number):
        if number % prime == 0:
            print(prime)

def calculate_fast(number):
    """
    Find the largest prime, quickly
    """
    print("TODO")

calculate_slow(13195)
