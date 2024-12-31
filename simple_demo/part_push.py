#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-30 01:20'

"""
100个元素列表，每10个一组分段逆序打印（提交）
"""

# l0 = [i for i in range(0,133)]
l0 = [i for i in range(0,100)]

print(l0)
print(len(l0))

l0.reverse()  # 注意使用reverse()后l0已经变化
print(l0)

group_list = [ l0[i:i+10] for i in range(0,len(l0),10) ]

print(group_list)

print("-"*77)

for group in group_list:
    print(group)