#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/14 21:48'

"""
HJ7 -- 取近似值

https://www.nowcoder.com/practice/3ab09737afb645cc82c35d56a5ce802a?tpId=37&&tqId=21230&rp=1&ru=/activity/oj&qru=/ta/huawei/question-ranking

题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值

思路：1.首先将输入的浮点型数乘以10，然后整除10求余数（%），判断余数和5的大小，输出整数。

# 5.5 -> 6
"""

a = float(input())
b = a*10
c = 0

if b%10 >=5:
    c = int(a) + 1
else:
    c = int(a)

print(c)


