#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/14 22:35'

"""
HJ1 -- 字符串最后一个单词的长度
(Python解答是简单级别)

https://www.nowcoder.com/practice/8c949ea5f36f422594b306a2300315da?tpId=37&&tqId=21224&rp=1&ru=/activity/oj&qru=/ta/huawei/question-ranking

题目描述
计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
一行字符串，非空，长度小于5000。

输出描述:
整数N，最后一个单词的长度。

"""

print(len(input().split(' ')[-1]))