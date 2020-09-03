# coding=utf-8
'''
DATE: 2020/09/03
AUTHOR: Yanxi Li
'''

import array

# 2-5 用生成器表达式初始化元组和数组

symbols = '$¢£¥€¤'

ti = tuple(ord(symbol) for symbol in symbols)
print(ti)

ai = array.array('I', (ord(symbol) for symbol in symbols))

print(ai)
