#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-21 22:24'

"""
Python如何以两个字符一行方式输出"Hello World"(包括空格)
"""
def f(string):
    st = ''
    for i in range(len(string)):

        if (i + 1) % 2 != 0:
            st = st + string[i]
            if len(string) == (i + 1):
                print(st)
        else:
            st = st + string[i]
            print(st)
            st = ''


if __name__ == '__main__':

    input_str = 'hello world'
    f(input_str)




