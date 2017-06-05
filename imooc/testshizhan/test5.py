#!/usr/bin/env python
#coding=utf-8

# __author__ = 'yanxi'
'''
实战 Python分布式爬虫打造搜索引擎 Scrapy精讲
http://coding.imooc.com/lesson/92.html#mid=2845
'''

import re

line = "study in 上海交通大学"
regex_str = ".*?([\u4E00-\u9FA5]+大学)"
# \s 代表匹配单个空格。 \S 代表匹配单个非空格  ＋至少匹配1个或以上
# ?限定后面内容为非贪婪匹配模式，即正向匹配
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))   # 以最外层括号为顺序