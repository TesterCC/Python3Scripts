#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/30 17:52'

'''
Python基础班
C1 02-19 19-break和continue

continue demo
'''

i = 1

while i <= 10:
    i += 1

    print("---------")

    if i == 3:
        # break    # 结束整个while循环
        continue   # 结束这一次的循环，转而执行下一次的循环

    print(i)


print("============")