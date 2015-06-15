#!/usr/bin/python3
# -*- coding: utf-8 -*-


def pow(x, n=2):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')
    if not isinstance(n, int):
        raise TypeError('Bad operand type')
    res = 1
    while n > 0:
        res = res * x
        n = n - 1
    return res

n = input('Please input a number: ')
print(pow(int(n)))
