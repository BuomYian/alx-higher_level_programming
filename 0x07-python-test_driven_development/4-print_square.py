#!/usr/bin/python3
"""

This module contain a function that prints a square

"""

def print_square(size):
    '''This function prints square with the character #

    Args:
        size: is the size length of the square

    Raises:
        TypeError: If size must be an integer
        ValueError: If size must be >= 0
        TypeError: If size is a float and less than zero

    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
