#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-05-10 19:28'


"""
攻防世界：
c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2

16进制转str脚本

解题思路：

首先，2个一组（如：c8、e9、ca...）做转换为10进制数。

然后，将十进制数模128（因为ASCII码值为0-127），让其落到ASCII码表上，计算出对应ASCII码值的字符。
"""

enstr = "c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2"

print(len(enstr))

flag = ""

while len(enstr):
    flag = flag + chr(int(enstr[:2],16)%128)   # int() 函数用于将一个字符串或数字转换为整型。
    enstr = enstr[2:]

print(flag)


