#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/15 13:45'

"""
边界匹配
"""

import re

qq = '100000001'

# 4-8
r = re.findall('\d{4,8}', qq)

r2 = re.findall('^\d{4,8}$', qq)

r3 = re.findall('^000', qq)

r4 = re.findall('000$', qq)

print(r)
print(r2)
print(r3)
print(r4)
