#!/usr/bin/env python
# coding:utf-8
#__author__ = 'Yanxi'

import re

line = "bobby123"
regex_str = "^b.*3$test.py"    # 以B开头,以任意字符且不限数量结尾, . 代表任意字符, * 代表前面字符可以重复多遍
if re.match(regex_str, line):
    print("yes")
else:
    print("no")
