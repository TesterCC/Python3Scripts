#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/3 12:58'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000

版本2:
版本二可以验证并提取出带名字的Email地址：

<Tom Paris> tom@voyager.org

"""

import re

email_list = ["<Tom Paris> tom@voyager.org", "<Mary Hans> mary520@voyager.net"]

email_str1 = "<Tom Paris> tom@voyager.org"

email_str2 = "<Mary Hans> mary520@voyager.net"


regex_mail = re.compile(r"^<[a-zA-Z]+\s[a-zA-Z]+>\s([a-zA-Z0-9_.]+)@([a-zA-Z0-9_]{2,20}).(\w{2,3})$")

print(regex_mail.match(email_str1).group(0))
print(regex_mail.match(email_str2).group(0))

# 最终调试
match_result = [regex_mail.match(email_str).group(0) for email_str in email_list]
print(match_result)