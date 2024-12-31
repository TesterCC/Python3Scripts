#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-12 17:47'

import jieba

"""
使用样本：
English Sample: https://python123.io/resources/pye/hamlet.txt
Chinese Sample: https://python123.io/resources/pye/threekingdoms.txt
"""

# CalThreeKingdomsV1.py
txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
