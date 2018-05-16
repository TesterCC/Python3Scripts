#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/17 00:44'

"""
在线正则调试：http://regex.zjmainstay.cn/

test txt:
17033554433
13551856640
15282102310
13658089791
17730338094
16630289990
19133302930  (don't match)

https://blog.csdn.net/hs947463167/article/details/79463668
"""

import re

# 验证手机号是否正确

# phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
# update phone regex
phone_pattern = re.compile('^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$')

phone_list = ['17730338094', '16630289990', '19133302930']


# while True:
#     phone = input('请输入您的手机号:')

for phone in phone_list:

    phone = phone.strip()

    res = re.search(phone_pattern, phone)
    if res:
        print('{} -- 正常手机号'.format(phone))
    else:
        print('{} -- 异常手机号'.format(phone))