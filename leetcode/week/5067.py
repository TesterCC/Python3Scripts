#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-09-07 22:32'

"""
5067. 统计只含单一字母的子串 显示英文描述 
用户通过次数0
用户尝试次数0
通过次数0
提交次数0
题目难度Easy
给你一个字符串 S，返回只含 单一字母 的子串个数。

输入： "aaaba"
输出： 8
解释： 
只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
"aaa" 出现 1 次。
"aa" 出现 2 次。
"a" 出现 4 次。
"b" 出现 1 次。
所以答案是 1 + 2 + 4 + 1 = 8。

输入： "aaaaaaaaaa"
输出： 55
"""

from collections import Counter
from itertools import accumulate

# S = "aaaaaaaaaa"
S = "aaaba"
# print(Counter(S))



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3.6
from itertools import accumulate

def all_sub_string(a_string):
    if len(a_string) == 1:
        return [a_string]
    else:
        return list(accumulate(a_string)) + all_sub_string(a_string[1:])



all_sub_strs = all_sub_string(S)
print(all_sub_strs)

ms = dict(Counter(S))
# print(ms)

ret = 0
for k,v in ms.items():
    while v > 0:
        for i in k*v:
            ch = i*v
            for ch in all_sub_strs:
                if ch in all_sub_strs:
                    print(ch)
                    all_sub_strs.remove(ch)
                    ret+=1
            v -= 1

print(ret)

