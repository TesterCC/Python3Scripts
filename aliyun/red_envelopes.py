#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/3/1 22:41'

"""
python实现的抢红包程序代码
https://yq.aliyun.com/ziliao/43578

其中一种拼手气红包，发红包时用户输入一个红包总金额和待发红包总数，发布红包后，其它用户抢红包时可以随机得到不定金额的红包，
RP好的可能抢到几块，RP不好时可能只会抢到几毛，甚至几分钱。
"""

import random
import sys


def calRandomValue(total, num):  # total 红包总金额, num 抽红包的人数
    """
    计算随机值
    :param total:
    :param num:
    """
    total = float(total)
    num = int(num)
    min = 0.01   # 基数
    if num < 1:
        return
    if num == 1:
        print("第%d个人拿到红包数为：%.2f" % (num, total))
        return

    i = 1
    while i < num:
        max = total - min*(num-i)
        k = int((num-i)/2)
        if num - i <= 2:
            k = num - i
        max = max/k
        monney = random.randint(int(min * 100), int(max * 100))
        monney = float(monney) / 100
        total = total - monney
        print("第%d个人拿到红包数为：%.2f, 余额为: %.2f" % (i, monney, total))
        i += 1

    print("第%d个人拿到红包数为：%.2f, 余额为: %.2f" % (i, total, 0.0))


if __name__ == '__main__':
    total = input('输入红包总金额:')
    num = input('输入发红包数量:')
    calRandomValue(total, num)


