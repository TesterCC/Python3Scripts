# coding:utf-8
__author__ = 'Yanxi'

import re

line = "boooooooobby123"
regex_str1 = ".*(b.*b).*"    # 贪婪匹配,从后往前匹配
regex_str2 = ".*?(b.*b).*"    # 加入?--非贪婪匹配,从前向后匹配
regex_str = ".*?(b.*?b).*"    # 加入?--非贪婪匹配,从前向后匹配
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
else:
    print("no")
