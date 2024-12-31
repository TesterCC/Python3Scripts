#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/5/21 17:19'

'''
a simple method to generate tiny-url
10 -> 62

递增序列算法
'''

CHARS="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def tiny_url_encode(num):
    # 10进制->62进制
    if num == 0:
        return CHARS[0]
    res = []   # 保存二进制串的列表
    while num:
        num, rem = divmod(num, len(CHARS))   # 对 CHARS的长度62  取余数,rem表示余数，num表示商
        res.append(CHARS[rem])
    return ''.join(reversed(res))


if __name__ == '__main__':

    print(tiny_url_encode(0))
    print(tiny_url_encode(31))
    print(tiny_url_encode(61))
    print(tiny_url_encode(62))