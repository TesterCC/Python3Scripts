#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-05-05 11:26'

"""
ref:
https://docs.python.org/zh-cn/3/library/argparse.html
https://docs.python.org/zh-cn/3/howto/argparse.html


run in terminal:

python argparse_demo.py -h  
python argparse_demo.py --help
python argparse_demo.py foo  

在没有任何选项的情况下运行脚本不会在标准输出显示任何内容。这没有什么用处。

第二行代码开始展现出 argparse 模块的作用。我们几乎什么也没有做，但已经得到一条很好的帮助信息。

--help 选项，也可缩写为 -h，是唯一一个可以直接使用的选项（即不需要指定该选项的内容）。指定任何内容都会导致错误。即便如此，我们也能直接得到一条有用的用法信息。
"""

import argparse

parser = argparse.ArgumentParser()

# 位置参数
# parser.add_argument("echo")

# 增加位置参数的说明
parser.add_argument("echo", help="echo the args you use here")
parser.add_argument("square", help="display a square of a given number",type=int)   # 指定类型

# 可选参数
parser.add_argument("--verbosity", help="increase output verbosity",action="store_true")
# 指定了一个新的关键词 action，并赋值为 "store_true"。这意味着，当这一选项存在时，为 args.verbose 赋值为 True。没有指定时则隐含地赋值为 False。
# 如果一个可选参数没有被使用时，相关变量被赋值为 None

args = parser.parse_args()

if args.verbosity:
    print('verbosity turned on')

print(args.echo)
print(args.square**2)
# 运行 python argparse_demo.py foo 能打印出foo


# python argparse_demo.py test 3
# python argparse_demo.py test 3 --verbosity x
