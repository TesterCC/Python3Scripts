#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/18 01:29'

"""
正则替换  用函数处理
"""

import re

language = 'PythonC#JavaC#PHPC#'


def convert(value):
    """
    covert is null, so replace C# is null
    :param value:
    :return:
    """
    pass


r = re.sub('C#', convert, language)  # 匹配到C#并传给函数convert处理

print(r)

r = re.sub('C#', convert, language, 2)  # 匹配到C#并传给函数convert处理，只进行前2个的替换

print(r)
