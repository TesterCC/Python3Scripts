# coding=utf-8
"""
DATE:   2021/2/2
AUTHOR: Yanxi Li

# 别人的练习程序，改来看看
"""

import sys
import subprocess

i = 0

while True:
    i += 1
    if i <= 50:
        print("------------------")
        print("i:%d" % i)
        subprocess.run("python ./print_demo.py")
    else:
        sys.exit()
