#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


import math
import random

a = math.pi
b = random.random()
c = random.randint(1, 10)

__name__ == '__main__'

start = input('from which number ?:')
end = input('end to which number ?:')
randint = random.randint(int(start), int(end))

print('PI is :' + str(a))
print('B is :' + str(b))

print('random number between   ' + str(start) + '   and    ' + str(end) + '  is   ' + str(randint))
