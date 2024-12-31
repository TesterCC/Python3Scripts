#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/20 13:27'

"""
斐波纳契数列以如下被以递推的方法定义：
F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

斐波拉契数列: 
0 1 1 2 3 5 8 13 21 34

9-3 08:29
"""

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)

def fib2(index):
    re_list = []       # 缺点：如果list很大，将非常消耗内存
    n, a, b = 0, 0, 1   # 初始化3个值
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list

def gen_fib(index):
    n, a, b = 0, 0, 1   # 初始化3个值
    while n < index:
        yield b       # 这里没有用list，不会消耗内存, yield值出来
        a, b = b, a+b
        n += 1

if __name__ == '__main__':

    print(fib(10))  # 直接打印出数列第10位的值

    print("*" * 50)

    print(fib2(10))

    print("*" * 50)

    fib_list = [data for data in gen_fib(10)]
    print(fib_list)



