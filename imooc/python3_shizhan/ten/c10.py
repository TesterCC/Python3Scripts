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

r = re.findall('python{1,2}', a)     # 最后一位n匹配1次或2次,默认贪婪模式
print(r)

r1 = re.findall('python{1,2}?', a)     # 最后一位n匹配1次或2次,设置为非贪婪模式
print(r1)








