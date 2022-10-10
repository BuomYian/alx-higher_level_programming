#!/bin/usr/python3
def safe_print_integer(value):
    try:
        print("{:d}".format())
        return True
    except Exception:
        return False
