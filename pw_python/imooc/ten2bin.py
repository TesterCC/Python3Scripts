#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/5/21 17:19'

def mybin(num):
    # 10进制->2进制
    if num == 0:
        return 0
    res = []   # 保存二进制串的列表
    while num:
        num, rem = divmod(num, 2)   # 对2取余数,rem表示余数，num表示商
        res.append(str(rem))
    return ''.join(reversed(res))


if __name__ == '__main__':

    for i in range(11):
        print(mybin(i))