#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/8 21:50'


"""
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
过滤非回文数

“回文”是指正读反读都能读通的句子，它是古今中外都有的一种修辞方式和文字游戏，如“我为人人，人人为我”等。
在数学中也有这样一类数字有这样的特征，成为回文数（palindrome number）
"""

# 好理解的简单写法
# def is_palindrome(n):
#     while n > 10:
#         n = str(n)
#         m = n[::-1]    ＃ 字符串倒叙
#         return n == m


# 优化写法
def is_palindrome(n):
    return str(n) == str(n)[::-1] and n > 10


# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))







