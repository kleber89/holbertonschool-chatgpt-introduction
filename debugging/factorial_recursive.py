#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
    Calculate the factorial of a given number.

    Parameters:
    - n (int): The number whose factorial needs to be calculated.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Obtain the factorial of the number passed as command-line argument
f = factorial(int(sys.argv[1]))
print(f)
