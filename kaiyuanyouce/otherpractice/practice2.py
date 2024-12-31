#!/usr/bin/python env
# coding:utf-8

import itertools
import time

'''
计算0123456789，无重复组合的十位数
'''

data = []
start = time.time()

for i in itertools.permutations('1234567890', 10):
    if i[0] != '0':
        # data.append("".join(i)) # i is tuple,so join
        data.append(i)

end = time.time()
print(end-start)
print(len(data))
print(type(data))
