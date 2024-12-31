#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-05 17:26'

"""
打印输出附件latex.log文件的有效行数，注意：空行不计算为有效行数。
"""

f = open("latex.log")
s = 0
for line in f:
    line = line.strip('\n')
    if len(line) == 0:
        continue
    s += 1
print("共{}行".format(s))