#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/2 21:37'

"""
Python3 正则表达式
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000
"""

import re

# 编译
# 在Python中使用正则表达式时，re模块内部会干两件事情：
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。

# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配
re_telephone = re.compile(r'^(\d{3,4})-(\d{3,8})$')  # 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用再给出正则字符串。

print(re_telephone.match('010-12345').groups())
print(re_telephone.match('0755-2812345').groups())




