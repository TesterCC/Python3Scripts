#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/30 17:50'


'''
Python基础班
C1 02-18 break、while里面用if

17.打印1-100之间的前20个偶数
'''

i = 1
num = 0
while i <= 100:
    # if i is even number
    if i % 2 == 0:
        print(i)
        num+=1

    if num == 20:
        break

    i += 1

