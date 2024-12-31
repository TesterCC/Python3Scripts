#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-05 17:26'

"""
打印输出附件latex.log文件的有效行数，注意：空行不计算为有效行数。
"""

count = 0
with open('latex.log', 'r', encoding='utf-8') as f:
    l = f.readlines()
    for line in l:
        line = line.strip('\n')
        if len(line) == 0:
            continue
        count += 1
    print("共{}行".format(count))

