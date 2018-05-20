#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/20 23:56'

"""
正则表达式的单字符匹配

.	匹配任意1个字符（除了\n）
[ ]	匹配[ ]中列举的字符
\d	匹配数字，即0-9
\D	匹配非数字，即不是数字
\s	匹配空白，即 空格，tab键
\S	匹配非空白
\w	匹配单词字符，即a-z、A-Z、0-9、_
\W	匹配非单词字符
"""

import re

ret = re.match(".", "a")
print(ret.group())

ret = re.match(".", "b")
print(ret.group())

ret = re.match(".", "M")
print(ret.group())


