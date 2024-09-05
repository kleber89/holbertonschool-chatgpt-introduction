#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) < 2:
    print("Please provide a number as a command line argument.")
else:
    f = factorial(int(sys.argv[1]))
    print(f)
