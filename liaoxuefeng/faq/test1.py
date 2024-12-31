#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/1 13:58'


"""
FAQ 本节列出常见的一些问题。
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143278155868605a65e244e6642dfa533753e6338ab5b000
"""

import os
import sys


# 如何获取当前路径 -- 当前路径可以用'.'表示，再用os.path.abspath()将其转换为绝对路径
print("获取当前路径")
print(os.path.abspath('.'))    # 获取当前路径, 到文件夹为止


# 如何获取当前模块的文件名 -- 可以通过特殊变量__file__获取
print("获取当前模块的文件名")
print(__file__)


# 如何获取命令行参数 -- 可以通过sys模块的argv获取
print("获取命令行参数")
print(sys.argv)
# python3 test.py -a -s "Hello world"
# argv的第一个元素永远是命令行执行的.py文件名


# 如何获取当前Python命令的可执行文件路径 -- sys模块的executable变量就是Python命令可执行文件的路径
print("获取当前Python命令的可执行文件路径")
print(sys.executable)
