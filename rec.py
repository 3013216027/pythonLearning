#!/usr/bin/python3
# -*- coding: utf-8 -*-


# A simple recuserve function
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

print(fact(100))
