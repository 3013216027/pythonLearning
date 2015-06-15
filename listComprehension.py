#!/usr/bin/python3
# -*- coding: utf-8 -*-


# At range [1, 11)
print([x for x in range(1, 11)])
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 1])

print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
