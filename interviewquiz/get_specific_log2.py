#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/16 22:03'


'''
请问一个日志文本文件有2000行，我要提取其中的100行到200行，怎么做？ 

生成器在处理文件中的应用，对于大文件，10几G的文本文件，处理效率高。

https://www.douban.com/group/topic/42996147/
'''

# success


f2 = open("get_specific.log", 'w')

def getLine(filepath):
    f1 = open(filepath, 'r')
    while True:
        line = f1.readline()
        yield line
        if not line:
            break
    f1.close()

list1 = list(getLine("testlog.log"))
f2.writelines(list1[99:200])     # 从0开始，第100个是index 99
# f2.writelines(list1[100:201])  # 从0开始，取日志第100到200行
f2.close()

print("Get specific lines log success.")