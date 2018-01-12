#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/11 23:10'


"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484023&idx=2&sn=62e946786e2c5327f44a4d49da5ed75b&scene=19#wechat_redirect
"""


def iftest():

    var = int(input(u"请输入一个整数:"))

    if 0 < var < 10:
        print(u"你输入的是一个大于0小于10的整数")
    elif var >= 10:
        print(u"你输入的是一个大于等于10的整数")
    else:
        print(u"你输入的是一个负数")


if __name__ == '__main__':
    iftest()

