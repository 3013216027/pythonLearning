#Note

##If-Loop
```python
if condition:
elif condition2:
else:

for x in []:

for x in range(101)

while condition:
   do something

!tag: str in python is something like 字符串产量池 in Java
```
---

##List(something like vector)
```python
L = ['a', 23, 'b']

L.append('c')
L.insert(1, 'd')

L.pop()
L.pop(1)
```

##Tuple(constant)
```python
T = ('a', 'b')
T2 = (1,)
T3 = ()

print(T[1])
```
##Dict, Set
```python
d = {'a':1, 'b':2}
print(d('a'))

s = set([1,2,3])
print(s)

s.add(4)
s.remove(2)

s2 = set([2,3,4])
print(s & s2)
print(s | s2)
```

##Functions
###Built-in Functions
[Python Built-in Functions](https://docs.python.org/3/library/functions.html#object)
####Here are them:
abs()	dict()	help()	min()	setattr()

all()	dir()	hex()	next()	slice()

any()	divmod()	id()	object()	sorted()

ascii()	enumerate()	input()	oct()	staticmethod()

bin()	eval()	int()	open()	str()

bool()	exec()	isinstance()	ord()	sum()

bytearray()	filter()	issubclass()	pow()	super()

bytes()	float()	iter()	print()	tuple()

callable()	format()	len()	property()	type()

chr()	frozenset()	list()	range()	vars()

classmethod()	getattr()	locals()	repr()	zip()

compile()	globals()	map()	reversed()	__import__()

complex()	hasattr()	max()	round()

delattr()	hash()	memoryview()	set()

---
###Rules
```python
import math


def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny
#	In fact, it returns a tuple!

# more about function: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000
```

#### Slice:
```python
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
```

####Iter
```python
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
```

####ListComprehension
```python
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
```
