#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Calculate a^2+b^2+...
def calc(*numbers):
    sum = 0
    for x in numbers:
        sum = sum + x * x
    return sum


print(calc(1, 2, 3, 4, 5))
print(calc(*[1, 2, 3, 4]))
print(calc(*[1, ]))


# Print personal imformation
def person(name, age, **others):
    if 'city' in others:
        pass
    elif 'girlfriend' in others:
        pass
    else:
        pass
    print('name:', name, 'age:', age, 'other:', others)


person('zhengdongjian', 20, height=165, weight=55)
person('mawenya', 24, height=166, weight=50)
person('libingyi', 23, height=166, weight=80)
extra = {'height': 166, 'girlfriend': 'Jianghui'}
person('yy', 22, **extra)  # pass a copy of extra

# Limit the argc name
def person2(name, age, *, city, weight):
    print(name, age, city, weight)

person2('zhengdongjian', 20, city='Tianjin', weight='165')
