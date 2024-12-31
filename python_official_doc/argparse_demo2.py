#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-05-05 21:10'

"""
ref:
https://docs.python.org/zh-cn/3/library/argparse.html
https://docs.python.org/zh-cn/3/howto/argparse.html


run in terminal:

python argparse_demo2.py -h  
python argparse_demo2.py --help
python argparse_demo2.py foo  

在没有任何选项的情况下运行脚本不会在标准输出显示任何内容。这没有什么用处。

第二行代码开始展现出 argparse 模块的作用。我们几乎什么也没有做，但已经得到一条很好的帮助信息。

--help 选项，也可缩写为 -h，是唯一一个可以直接使用的选项（即不需要指定该选项的内容）。指定任何内容都会导致错误。即便如此，我们也能直接得到一条有用的用法信息。
"""

import argparse

parser = argparse.ArgumentParser()

# 定义短选项
parser.add_argument("-v","--verbose",help="increase output verbosity",action="store_true")

args = parser.parse_args()

if args.verbose:
    print("verbosity turned on")