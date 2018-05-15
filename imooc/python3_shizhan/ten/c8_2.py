#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/15 13:33'

"""
10-5 数量词
* 匹配0次或无限多次
+ 匹配1次或无限多次
? 匹配0次或匹配1次
"""

import re

a = 'pytho0python1pythonn2'

r = re.findall('python*', a)     # 最后一位n匹配0次或无限多次
print(r)

r1 = re.findall('python+', a)     # 最后一位n匹配1次或无限多次
print(r1)

r2 = re.findall('python?', a)     # 最后一位n匹配0次或匹配1次,匹配上就会显示匹配的部分
print(r2)







