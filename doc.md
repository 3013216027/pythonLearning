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
```
