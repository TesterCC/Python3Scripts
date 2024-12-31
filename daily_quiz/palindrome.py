#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/3/30 23:12'

"""
3月29日 每日一题

用户输入一个字符串，程序来判断是否是『回文诗』（即无论正读、反读，内容完全一致）
字符串并不必须为中文，可以是数字、英文、符号等。
"""


def search_palindrome(content):
    content = str(content)
    _list = [i for i in content]
    _list.reverse()
    search = ''.join(_list)
    if content == search:
        print("这是回文字符")
    else:
        print("非回文字符")


if __name__ == '__main__':
    search_palindrome("33223044032233")
    search_palindrome("110311")
    search_palindrome("tooot")
    search_palindrome("abcdec")

