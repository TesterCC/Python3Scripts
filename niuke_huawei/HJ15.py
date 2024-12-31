#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/14 21:28'


"""
HJ15 -- 求int型数据在内存中存储时1的个数

https://www.nowcoder.com/practice/440f16e490a0404786865e99c6ad91c9?tpId=37&&tqId=21238&rp=1&ru=/activity/oj&qru=/ta/huawei/question-ranking

题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数
"""
# 5 -> 2
print(bin(int(input())).count('1'))

# 如果是计算0的个数，需要另行处理，因为bin把数字转为二进制后在二进制的前面会有0b，如数字8：0b1000，所以计算0需要减去1
