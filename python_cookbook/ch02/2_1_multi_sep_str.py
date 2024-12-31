# -*- coding: utf-8 -*-
# @Time    : 2022/5/11
# @Author  : SecCodeCat

"""
《Python+Cookbook》第三版中文v3.0.0
2.1 使用多个界定符分割字符串

问题:
将一个字符串分割为多个字段，但是分隔符还有周围的空格并不是固定

解决方法：
用re.split()
"""

import re

line = 'asdf fjdk; afed,fjek,asdf,  foo'

# 正则模式意思：分隔符可以是逗号，分号或者是空格，并且后面紧跟着任意个的空格
# 模式匹配
ret = re.split(r'[;,\s]\s*', line)
print(ret)

# ()表示捕获分组
ret = re.split(r'(;|,|\s)\s*', line)
print(ret)

# 保留分割字符，重新拼接输出
fields = 'asdf fjdk; afed,fjek,asdf,  foo'
fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::2]
delimiters = fields[1::2] + [' ']
print(values)
print(delimiters)

# reform the line using the same delimiters
ret = ''.join(v + d for v, d in zip(values, delimiters))
print(ret)

line = 'asdf fjdk; afed,fjek,asdf,  foo'
# 不保留分割字符串到结果列表中去,非捕获分组，形如(?:...)
ret = re.split(r'(?:,|;|\s)\s*', line)
print(ret)
