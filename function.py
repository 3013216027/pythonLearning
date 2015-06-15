#!/usr/bin/python3
# -*- coding: utf-8 -*-


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x < 0:
        x = -x
    return x

n = input('Please input a number: ')
print(my_abs((n)))
