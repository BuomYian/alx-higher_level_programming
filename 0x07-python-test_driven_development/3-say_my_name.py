#!/usr/bin/python3
"""

This module contain function that prints name

"""
def say_my_name(first_name, last_name=""):
    '''This function prints name (<first_name> <last_name>)

    Args:
        first_name: the first name to be printed
        last_name: the last name to be printed

    Raises:
        TypeError: If either the first_name or last_name are not str

    '''	
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
