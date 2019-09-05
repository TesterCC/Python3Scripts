#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-28 19:51'


"""
python的随机，random已经很好用了，不要因为需求复杂，就被绕晕
"""

from collections import Counter
import random

result = []

for i in range(10000):
    result.append(random.choice(range(3)))


print(len(result))
print(Counter(result))

result2 = []
for i in range(10000):
    result2.append(random.choice([0,1,2]))


print(len(result2))
print(Counter(result2))