#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-05-05 21:10'

"""
ref:
https://docs.python.org/zh-cn/3/library/argparse.html
https://docs.python.org/zh-cn/3/howto/argparse.html


run in terminal:

python argparse_demo6.py -h  
python argparse_demo6.py 2 2
python argparse_demo6.py -v 2 3 
python argparse_demo6.py -vv 2 3

矛盾的选项
"""

import argparse

parser = argparse.ArgumentParser()

# 第三个方法 add_mutually_exclusive_group()。 它允许我们指定彼此相互冲突的选项。

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

# 另一种动作 count，来数某一个可选参数出现了几次. 如果你不添加 -v 标志，这一标志的值会是 None。
parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
# 默认情况下如果一个可选参数没有被指定，它的值会是 None，并且它不能和整数值相比较

args = parser.parse_args()
answer = args.x ** args.y

# 目前一直在使用详细级别来 更改 所显示的文本
if args.verbose >= 2:  # python argparse_demo3.py 4 -v 2
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
    print("Running '{}'".format(__file__))   # 增加详细现实信息
elif args.verbose == 1:  # python argparse_demo3.py 4 -v 1
    print("{}^{} == {}".format(args.x, args.y, answer))
else:
    print(answer)
