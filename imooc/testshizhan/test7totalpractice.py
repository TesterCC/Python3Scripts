#!/usr/bin/env python
#coding=utf-8

# __author__ = 'yanxi'
'''
实战 Python分布式爬虫打造搜索引擎 Scrapy精讲
http://coding.imooc.com/lesson/92.html#mid=2845
综合练习
'''

import re

# line = "XXX出生于2001年6月1日sdfs"
# line = "XXX出生于2001_06_30"
# line = "XXX出生于2001/6/30ddd"
# line = "XXX出生于2001-6-1"
line = "XXX出生于2001-06dd"
# line = "XXX出生于2001年6月"
line = "XXX出生于2001/6"

regex_str2 = ".*出生于(\d{4}[年/_-]\d{1,2}([月/_-]\d{1,2}([日]|$)|[月/_-]$|$))"  # 包含日的匹配,简

# regex_str3 = ".*出生于(\d{4}[年/_-]\d{1,2}([月/_-]\d{1,2}[日]|[月/_-]\d{1,2}$|[月/_-]$|$))"  # 包含日的匹配，繁


# \d{4}[年/-_.]
# \d{1,2}([月/_-]\d{1,2}([日]|$)|[月/_-]$|$)


# lesson regex
# regex_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))"      # 教程标准 \d  小写d代表匹配单个数字

match_obj = re.match(regex_str2, line)
if match_obj:
    print(match_obj.group(1))   # 以最外层括号为顺序