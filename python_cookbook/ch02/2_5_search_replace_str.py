#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/19 22:57'

"""
《Python+Cookbook》第三版中文v3.0.0   
2.5 字符串搜索和替换    P55

问题:
在字符串中搜索和匹配指定的文本模式
"""

# simple mode, use replace()

text = 'Go is a wonderful language, Go is my favorite, You should learn Go'

ret = text.replace("Go", "Python")

print(ret)

# complex mode, use re.sub()

text = 'Today is 08/20/2018, Python practice starts 10/24/2018.'

import re

ret = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

print(ret)