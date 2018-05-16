#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/16 15:04'

import re


# keyword = u'13558888888'
keyword = u'17033554433 \n'
# keyword = u'\n13558888888 '

# 正则匹配中国电话话号
# p = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')   # 漏掉部分手机号

# https://blog.csdn.net/voidmain_123/article/details/78962164
# 最新、最全、最准确的手机号正则表达式
# p = re.compile('^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\\d{8}$')  # java use
p = re.compile('^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$')

phone_match = p.match(keyword.strip())    # 简单处理下空格和转义符

if phone_match:
    print(phone_match.group())
    print(type(phone_match.group()))
else:
    print("Phone number is error!")

