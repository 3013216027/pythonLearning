#!/usr/bin/python3
# -*- coding: utf-8 -*-

L = [1, 2, 3, 4, 5, 6, 7]

i = 0
while i < 3:
    print(L[i])
    i = i + 1

print(L[0:3])
print(L[-1:])
print(L[-2:])
print(L[::3])  # Choose numbers in each 3 ones
print('ABCDEFG'[:3])
print('ABCDEFG'[4:3])
print('ABCDEFG'[-2:])
print('ABCDEFG'[::3])
