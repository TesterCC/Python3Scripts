#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/30 18:14'


'''
Python基础班
C1 20-while嵌套中的break作用范围
'''


i = 1

while i <= 5:
    j = 1        # 控制*符号数量
    while j <= i:
        print('*', end="")
        j += 1
        break     # 结束当前while循环，不影响外层while循环

    print("")   # 换行
    i += 1

