#!/usr/bin/env python
# coding:utf-8


import re
from collections import Counter

# http://coding.imooc.com/lesson/62.html#mid=837
# 2. 对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，它们出现次数是多少？
# 统计文章：Linux kernel coding style, coding_style.txt
# 地址：https://www.kernel.org/doc/html/latest/process/coding-style.html

txt = open("coding_style.txt").read()
# print(txt)

# 利用re以非字母进行词类分割
word = re.split('\W+', txt)
# print(word)

c3 = Counter(word)
print(c3)    # 显示全部分割词，按出现频率降序排词
print(c3.most_common(10))   # 出现次数最高的10个词   c3.most_commne() list object
print("Most common 10 words:\n" + str(c3.most_common(10)))
