#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Yanxi'

import re

line = "boooobaaaoooobaaby123"
regex_str = ".*(b.+b).*"    #
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
else:
    print("no")
