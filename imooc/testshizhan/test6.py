#!/usr/bin/env python
#coding=utf-8

# __author__ = 'yanxi'
'''
实战 Python分布式爬虫打造搜索引擎 Scrapy精讲
http://coding.imooc.com/lesson/92.html#mid=2845
'''

import re

line = "XXX出生于2001年"
# regex_str = ".*?(\d+)年"      # \d  小写d代表匹配单个数字
regex_str = ".*(\d{4})年"      # \d  小写d代表匹配单个数字

match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))   # 以最外层括号为顺序