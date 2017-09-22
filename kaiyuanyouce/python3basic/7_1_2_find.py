#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 22:41'


"""
字符串
https://note.youdao.com/web/#/file/WEB98c227493cf921f71d8b69ba93cef80d/note/WEB7f0ac39f04ec94e91ae095d9fadcc620/
在python3中，所有的字符串都是Unicode编码
find and replace
"""

if __name__ == "__main__":
    source_str = u"it's my book, please show it, wa ka ka, yo yo yo!"

    # 从左往右查找yo
    print(u"从左往右查找 yo")
    print(source_str.find("yo"))
    print(source_str.index("yo"))

    # 从右往左查找yo
    print(u"从右往左查找 yo")
    print(source_str.rfind("yo"))
    print(source_str.rindex("yo"))

    # 替换所有的 yo
    des_str = source_str.replace("yo", "ha")
    print(des_str)

    # 替换两次 yo
    des_str = source_str.replace("yo", "ha", 2)
    print(des_str)