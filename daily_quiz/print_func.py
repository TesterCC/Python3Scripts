# -*- coding: utf-8 -*-
# @Time    : 2022/9/4
# @Author  : SecCodeCat

def func(val1, val2=2, val3=7, val4=1):
    return val1 ** val2 ** val3       # 2**2**4 = 2**16


print(func(val2=2, val1=2, val3=4))   # 65536
