#!/usr/bin/python3
# -*- coding: utf-8 -*-


dic = {'a': 1, 'b': 2, 'c': 3}
for key in dic:
    print(key)

for value in dic.values():
    print(value)

for key, value in dic.items():
    print(key, value)

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance(dic, Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
