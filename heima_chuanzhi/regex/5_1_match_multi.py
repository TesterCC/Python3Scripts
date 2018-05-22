#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/22 17:47'

"""
匹配多个字符的相关格式
字符	功能  (根据是否是贪婪模式来定)
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,}	匹配前一个字符至少出现m次
{m,n}	匹配前一个字符出现从m到n次
"""

import re

# 需求1：匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
text1 = 'Mm'
text2 = 'Aabcdef'

ret = re.match("[A-Z][a-z]*", text1)
print(ret.group())

ret = re.match("[A-Z][a-z]*", text2)
print(ret.group())

# 需求2：匹配出，变量名是否有效

