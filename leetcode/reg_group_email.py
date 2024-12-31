#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-11 23:49'

# Python中正则匹配使用findall,捕获分组(xxx)和非捕获分组(?:xxx)的差异

import re

str1 = "123@qq.comaaa@163.combbb@126.comasdf111@asdfcom"

'''
findall函数，就是说在正则匹配里，如果有分组，就仅仅匹配分组里面的内容，然后返回这个组的列表; 
如果有多个分组，那就把每一个分组看成一个单位，组合为一个元组，然后返回一个含有多个元组的列表。
'''

re_a = r"\w+@(qq|163|126).com"
re_b = r"\w+@(?:qq|163|126).com"

regex_a = re.compile(re_a)
regex_b = re.compile(re_b)

print(regex_a.findall(str1))   # 是匹配了捕获组，所以得到了['qq', '163', '126'] 这个列表
print(regex_b.findall(str1))   # ?: 把捕获组转变为一个非捕获组，使得这个式子可以从头到尾全部匹配
