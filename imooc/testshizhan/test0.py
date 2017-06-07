#!/usr/bin/env python
#coding=utf-8

# __author__ = 'yanxi'
'''
实战 Python分布式爬虫打造搜索引擎 Scrapy精讲
http://coding.imooc.com/lesson/92.html#mid=2844
'''

import re

line = "18792912222"
regex_str = "(1[48357][^1]{9})"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))   # 以最外层括号为顺序

