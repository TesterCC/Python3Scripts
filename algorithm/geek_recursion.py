#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-23 11:45'


"""
Fibonacci array: 1,1,2,3,5,8,13,21,34,...
F(n)=F(n-1)+F(n-2)

非最优解，面试慎写
"""

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print(fib(6))     #  输出第6位的值