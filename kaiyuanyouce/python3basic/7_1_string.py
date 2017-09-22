#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 22:22'

"""
字符串
https://note.youdao.com/web/#/file/WEB98c227493cf921f71d8b69ba93cef80d/note/WEB7f0ac39f04ec94e91ae095d9fadcc620/
在python3中，所有的字符串都是Unicode编码
join and split
"""


if __name__ == '__main__':
    t = ('1', '2', '3', '4', '5', 'a', 'b', "efg")   # tuple

    # 用 - 将t中元素合并成一个新的字符串
    str_demo = '-'.join(t)
    print(str_demo)

    # 将str_demo以-进行切割
    str_set = str_demo.split('-')
    print(str_set)

    # 将t中元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)



