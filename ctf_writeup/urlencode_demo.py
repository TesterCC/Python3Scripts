#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-05-09 23:38'

"""ASCII转16进制
今天做CTF解二重编码遇到过

1.获取字符的ascii值
ord("a")       //获取到的值为97

2.10进制转16进制
hex(97)        // '0x61'
"""

def enstr2hex(init_str:str)->str:

    if not init_str:
        return "init_str cannot empty"

    ord_str = [hex(ord(i)) for i in init_str]

    ret_str = "".join([i.replace("0x","%")for i in ord_str])

    # print(f"function {enstr2hex.__name__} , debug print ret_str: {ret_str}")
    return ret_str


if __name__ == '__main__':
    print(enstr2hex("admin"))


