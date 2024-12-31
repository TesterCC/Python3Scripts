#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/30 17:52'

'''
Python基础班
C1 02-18 break、while里面用if

break demo
'''

i = 1

while i <= 5:
    print("---------")

    if i == 3:
        break    # 立即结束while循环执行

    print(i)

    i += 1

print("============")