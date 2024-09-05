#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Resta 1 en cada iteración
    return result

if len(sys.argv) < 2:
    print("Please provide a number as a command line argument.")
else:
    f = factorial(int(sys.argv[1]))
    print(f)
