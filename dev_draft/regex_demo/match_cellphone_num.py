#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/16 15:04'

import re


keyword = u'13558888888'    # http://www.iplaypy.com/code/mobile/m5745.html
# keyword = u'\n13558888888 '

# 正则匹配中国电话话号
p = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')

phone_match = p.match(keyword.strip())    # 简单处理下空格和转义符

if phone_match:
    print(phone_match.group())
    print(type(phone_match.group()))
else:
    print("Phone number is error!")

