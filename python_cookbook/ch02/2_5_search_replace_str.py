#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/19 22:57'

"""
《Python+Cookbook》第三版中文v3.0.0   
2.5 字符串搜索和替换    P55

问题:
在字符串中搜索和匹配指定的文本模式

解决方法：
合理利用正则表达式的搜索和替换，sub()基本已经涵盖了所有

其实正则表达式最难的部分就是：编写正则表达式模式
"""

# Scenario 1: simple mode, use replace()

text = 'Go is a wonderful language, Go is my favorite, You should learn Go'

ret = text.replace("Go", "Python")

print(ret)

# Scenario 2: complex mode, use re.sub()
# 将形式为08/20/2018的日期字符串改成2018-08-20

text = 'Today is 08/20/2018, Python practice starts 10/24/2018.'

import re

ret = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
# sub()中第一个参数是被匹配的模式， 第二个参数是替换模式。反斜杠数字比如\3指向前面模式的捕获组号。

print(ret)

# Scenario 3: 如果打算用相同模式做多次替换，考虑先编译它来提升性能
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')

date = pattern.sub(r'\3-\1-\2', text)

print(date)


# Scenario 4: 对于更加复杂的替换，可以传递一个替换回调函数来代替。
from calendar import month_abbr


def change_date(m):
    """
    一个替换回调函数的参数是一个match对象，也就是match() or find()返回的对象。
    使用group()来提取特定的匹配部分。
    回调函数最后返回替换字符串。
    :param m:
    """
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


ret = pattern.sub(change_date, text)

print(ret)


# Scenario 5: 如果除了替换后的结果外,你还想知道有多少替换发生了,可以使用re.subn()来代替.

newtext, n = pattern.subn(r'\3-\1-\2', text)

print(newtext)

print(n)