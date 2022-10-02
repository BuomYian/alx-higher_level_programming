#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = 0
    for item in set(my_list):
        n += item
    return n
