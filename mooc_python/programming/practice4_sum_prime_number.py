#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-12 16:26'

"""

100以内素数之和
描述
求100以内所有素数之和并输出。 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬
素数指从大于1，且仅能被1和自己整除的整数。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

提示：可以逐一判断100以内每个数是否为素数，然后求和。


https://www.jb51.net/article/133459.htm
"""

value=2
num=0
for i in range(3,100):
    for k in range(i-1,1,-1):
        if i%k==0:
            num=0
            break
        else:
            num=1
    if num==1:
        value=value+i

print(value)


# Method 2 素数相加
N = 100
i = 2
num = 2
s = 0
for i in range(2, 100):
    for num in range(2, i):
        if (i % num == 0):   # 在非1和非自身的数中还有能整除的数，就说明这个是合数
            break
    else:
        s += i
print(s)


