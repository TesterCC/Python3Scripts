#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-22 14:22'

# 思考输出结果
def clear_list(l):
    l = []
    print(l)
    print(id(l))    # []

ll = [1,2,3]
clear_list(ll)
print(ll)    #  [1,2,3]
print(id(ll))    # id不同，


# Python可变参数作为默认参数
# 记住默认参数只计算一次

def flist(l=[1]):
    l.append(1)
    print(l)

flist()   # [1, 1]
flist()   # [1, 1, 1]



