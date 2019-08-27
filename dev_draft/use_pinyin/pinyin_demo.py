#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-27 10:54'


"""
https://pypinyin.readthedocs.io/zh_CN/master/
https://github.com/mozillazg/python-pinyin
"""
from pypinyin import pinyin, lazy_pinyin

print(pinyin("重庆"))
print(lazy_pinyin("重庆"))
print(lazy_pinyin("天津"))

s = "".join(lazy_pinyin("呼和浩特"))
print(s)