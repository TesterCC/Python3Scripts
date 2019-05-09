#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-09 11:57'

"""
汉诺塔  递归经典案例 理解了这个问题就基本理解递归了。
https://www.icourse163.org/learn/BIT-268001?tid=1206073223#/learn/content?type=detail&id=1210530408&cid=1212669776

flash game hanoi:
http://www.4399.com/flash/293_1.htm
"""

count = 0


def hanoi(n, src, dst, mid):
    global count  # 记录移动圆盘的步骤
    if n == 1:
        print("{}:{} -> {}".format(count+1, src, dst))
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print("{}:{} -> {}".format(count+1, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)


hanoi(4, 'a', 'c', 'b')
print(f"Total Steps: {count}")   # f-strings, support by python 3.6
