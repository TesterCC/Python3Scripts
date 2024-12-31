#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 23:01'

"""
字符串
https://note.youdao.com/web/#/file/WEB98c227493cf921f71d8b69ba93cef80d/note/WEB7f0ac39f04ec94e91ae095d9fadcc620/
在python3中，所有的字符串都是Unicode编码
判断字符串类型
"""

if __name__ == "__main__":
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "    "
    str_7 = " sfsdf "
    str_8 = "四五六"

    # isalnum
    print(str_3.isalnum())

    # isalpha
    print(str_2.isalpha())

    # isdigit
    print(str_1.isdigit())

    # islower
    print(str_4.islower())
    print(str_2.islower())

    # isupper
    print(str_4.isupper())
    print(str_2.isupper())

    # isspace
    print(str_6.isspace())
    print(str_7.isspace())

    # compare isdigit or isnumeric
    print(str_8.isdigit())    # False
    print(str_8.isnumeric())   # True