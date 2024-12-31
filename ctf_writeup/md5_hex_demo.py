#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-09-05 20:37'

"""
md5(？).hex[:6]=‘23333’

求？

[:6]意思是前六位

.hex()意思是做了一次hex编码

md5(?)意思是做了一次md5

分析一波，只能暴力枚举

python3
md5(str(15245815).encode("utf-8")).hexdigest()[:6] == '233333'
"""

from hashlib import md5
import time

# 虽然能暴力破解出来，但是，感觉时间很长，看下是否能优化
# for i in range(10**9):
for i in range(15245815, 15245900):
    if md5(str(i).encode("utf-8")).hexdigest()[:6] == '233333':
        print(i)
        break



