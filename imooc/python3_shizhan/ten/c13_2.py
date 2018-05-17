#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/18 01:05'

"""
正则模式

概括字符集

\d  数字字符   \D  非数字字符
\w  单词字符   \W  非单词字符
\s  空白字符   \S  非空白字符
.   匹配除换行符\n之外其他所有字符
"""

import re


language = 'PythonC#\nJavaPHP'

# re.I   它表示忽略大小写
# 参数为re.S    它表示“.”（不包含外侧双引号，下同）的作用扩展到整个字符串，包括“\n”
r = re.findall('c#.{1}', language, re.I | re.S)   # 忽略大小写  正则模式

print(r)



