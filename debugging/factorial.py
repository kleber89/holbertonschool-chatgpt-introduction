#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n == 0:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    try:
        # Convert the argument to an integer
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("The argument must be a non-negative integer")
    except ValueError as e:
        print(e)
        sys.exit(1)

    # Calculate and print the factorial
    f = factorial(n)
    print(f)
