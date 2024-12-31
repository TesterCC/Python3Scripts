#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-01 17:40'

"""
目内容：

定义函数countchar()按字母表顺序统计字符串中所有出现的字母的个数（允许输入大写字符，并且计数时不区分大小写）。

输入格式:字符串

输出格式：列表

输入样例：

Hello, World!

输出样例：

[0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]

提示：string.count(chr(ord('t')))
"""

# method 1
def countchar(string):
    a = [string.lower().count(chr(i)) for i in range(ord('a'), ord('z') + 1)]
    return a   # list

if __name__ == "__main__":
    string = input()
    print(countchar(string))