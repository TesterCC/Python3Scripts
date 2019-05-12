#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-12 17:31'

import jieba

"""
3种模式：
1.精确模式：文本精准且分开，不存在冗余 （最常用）      
2.全模式：把文本中所有可能的词语都扫描出来，有冗余     
3.搜索引擎模式：在精确模式基础上，对长词再次切分，存在冗余

PS：精确模式+搜索引擎模式 比较好
"""

s="中华人民共和国是砥砺前行的"
# 精确模式
ret1 = jieba.lcut(s)
print(ret1)

# 全模式
ret2 = jieba.lcut(s, cut_all=True)
print(ret2)

# 搜索引擎模式
ret3 = jieba.lcut_for_search(s)
print(ret3)

# 想分词词典增加新词
jieba.add_word("Pentest")