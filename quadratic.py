#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('Bad operand type!')
    if not isinstance(b, (int, float)):
        raise TypeError('Bad operand type!')
    if not isinstance(c, (int, float)):
        raise TypeError('Bad operand type!')

    if isinstance(a, int) and a == 0:
        raise ValueError('Bad Value: zero was found!')

    det = b * b - 4 * a * c
    if det == 0:
        return -b // (2 * a)
    elif det < 0:
        return None
    else:
        det = math.sqrt(det)
        x1 = (-b + det) // (2 * a)
        x2 = (-b - det) // (2 * a)
        if x1 > x2:
            return x2, x1
        else:
            return x1, x2

print(quadratic(2, 3, 1))   # =>(-0.5, -1.0)
print(quadratic(1, 3, -1))  # =>(1.0, -4.0)
