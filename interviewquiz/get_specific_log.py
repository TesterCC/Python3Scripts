#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/16 22:03'


'''
请问一个日志文本文件有2000行，我要提取其中的100行到200行，怎么做？ 

https://www.douban.com/group/topic/42996147/

Method 1   从0开始，99-199
'''


i = 0

f1 = open("testlog.log", 'r')
f2 = open("get_specific.log", 'w')

while True:
    line = f1.readline()
    i += 1
    if i>=100 and i <= 200:
        f2.write(line)
    if i > 200:
        break
    if not line:
        break

f1.close()
f2.close()

print("Get specific lines log success.")