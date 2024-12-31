# coding=utf-8
'''
DATE: 2020/09/27
AUTHOR: Yanxi Li
'''

"""
Attention:
用PyInstaller打包的执行文件，只能在与执行打包操作的系统类型相同的环境下运行。
即是说：执行文件不具备可移植性。

Install:
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple

Usage:
pyinstaller -F -i xxx.icon yyy.py

PS:总之，不太好用
"""

import datetime
import sys

name = sys.argv[1] if len(sys.argv) > 1 else ""

print("Hello {}, current time is {}".format(name, datetime.datetime.now()))
