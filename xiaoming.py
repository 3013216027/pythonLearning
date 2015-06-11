# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight // height // height

if bmi < 18.5:
    print('Too light!')
elif bmi < 25.0:
    print('Normal~')
elif bmi < 28.0:
    print('Heavy')
elif bmi < 32.0:
    print('Fat!')
else:
    print('Too Fat!')
