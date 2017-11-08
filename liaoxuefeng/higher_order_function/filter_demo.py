#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 18:28'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000
filter()
"""

# filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 在一个list中，删掉偶数，只保留奇数    even number偶数

print("---Who is odd---")


def is_odd(n):
    return n % 2 == 1    # 余数为1是奇数，余数为0是偶数


L = [1, 2, 4, 5, 6, 9, 10, 15]
r = list(filter(is_odd, L))
print(r)


print("---No Need Space---")


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

L2 = ['A', '', 'B', None, 'C', '  ']
r2 = list(filter(not_empty, L2))   # 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
print(r2)







