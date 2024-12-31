#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/2/15 12:49 
# @Author : MFC

"""
ref: https://www.bilibili.com/video/BV1u5411J7Th
# Q1: 2
# Q2: 6014760148
大数幂取模
欧拉定理：https://zhuanlan.zhihu.com/p/35060143
蒙哥马利算法：https://zhuanlan.zhihu.com/p/35242553
# Q3: 1-2+3*4*5+6*7*8+9
穷举即可
# Q4: in hacking8_v2.py
"""
import math
import time

x = 12345678910
n = 12345678901234567890
m = 9999999999


def relative_prime(m, n):
    # 判断x与m是否互质，辗转取余数
    while n != 0:
        r = m % n
        m = n
        n = r
    if m == 1:
        print("yes")
    else:
        print("no")


def fast_mod(x, n, m):
    '''
    蒙哥马利算法（快速幂取模算法） todo learn
    快速计算(x^n) mod (m)
    :param x:
    :param n:
    :param m:
    :return:
    '''
    res = 1
    x %= m
    while n:
        if n & 1:  # 如果 n&1 = 1，其二进制形式的最后一位等于1
            res = (res * x) % m
        n >>= 1  # 每一轮右移一位，就能得出其二进制每位是0还是1
        x = (x * x) % m
    print(res)


relative_prime(m, n)
print("Stage 2")
fast_mod(x, n, m)

print("Stage 3")
# 穷举法，for循环，4**8=65536
option = ['+','-','*','/']

eq = '1%s2%s3%s4%s5%s6%s7%s8%s9'

try_counts = math.pow(4, 8)

st = time.time()
for i in range(0, int(try_counts)):
    eq2 = []
    for j in range(0,8):
        eq2.append(option[(i >> (j * 2)) & 0x3])   # 使用按位操作简化了程序

    x = eq % tuple(eq2)
    if eval(x) == 404:
        print("Answer is：", x)

dt = time.time() - st
print("cost time: ", dt)