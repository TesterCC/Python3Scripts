#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/3 12:58'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000

版本1:
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

someone@gmail.com
bill.gates@microsoft.com

"""

import re

email_list = ["bill.gates@microsoft.com", "someone@gmail.com", "test203@foxmail.cc", "test_like00@qq.com"]

email_str1 = "someone@gmail.com"

email_str2 = "bill.gates@microsoft.com"

email_str3 = "test203@foxmail.cc"

email_str4 = "test_like00@qq.com"

regex_mail = re.compile(r"^([a-zA-Z0-9_.]+)@([a-zA-Z0-9_]{2,20}).(\w{2,3})$")

print(regex_mail.match(email_str1).group(0))
print(regex_mail.match(email_str2).group(0))
print(regex_mail.match(email_str3).group(0))
print(regex_mail.match(email_str4).group(0))

# 最终调试
match_result = [regex_mail.match(email_str).group(0) for email_str in email_list]
print(match_result)