#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/3/14 00:15'

"""
每日一题 2018年3月13日

你是一个软件开发者，现在需要随机生成50个激活码。写一个函数，其作用是根据参数生成激活码。

1. 唯一的参数为一个正整数
2. 函数生成的激活码由一串任意随机字符（英文大小写字母 + 数字）组成，且其长度等于参数值

最终效果如下：

def code_gen(length):
    pass
    assert len(activation_code) == length
    return activation_code
"""

from random import Random


# 初级解法
def code_gen(length=8):
    activation_code = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"   # 62
    tlength = len(chars) - 1    # 61, 从0开始计数
    random = Random()
    for i in range(length):
        activation_code += chars[random.randint(0, tlength)]
    return activation_code


if __name__ == '__main__':
    for i in range(50):
        print(code_gen())

