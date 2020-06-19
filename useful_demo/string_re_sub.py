#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/19 17:16'

"""
block word list 常用逻辑
"""

import re

block_word_list = ["啊","呜","666","P\.S\."]

block_word_pattern = "({})".format("|".join(block_word_list))

rel = "***"   # 把 block words 替换为 ***

# mock html text
html = '''
啊啊啊啊啊，美丽的田野，呜呜呜，秋风瑟瑟，让人忍不住想多录入几句666。记于2020年6月19日。
P.S.:测试脚本
'''

if re.search(block_word_pattern, html):   # 判断方便实现更多操作，如果只是需要实现替换，可以直接用re.sub
    print(1)
    ret = re.sub(block_word_pattern, rel, html)
    print(ret)
else:
    print(0)