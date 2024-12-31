#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/22 23:45'

"""
11-1 python 中的 GIL
GIL = global interpreter lock (in cpython)
python中一个线程对应于c语言中的一个线程
gil使得同一个时刻只有一个线程在一个cpu上执行字节码，无法将多个线程映射到多个cpu上执行
pypy是去gil化的 
"""

import dis


def add(a):
    a = a + 1
    return a


print(dis.dis(add))
