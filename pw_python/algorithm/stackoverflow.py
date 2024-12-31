#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/21 21:48'

def infinite_fib(n):
    return infinite_fib(n - 1) + infinite_fib(n - 2)

if __name__ == '__main__':

    infinite_fib(10)    # RecursionError: maximum recursion depth exceeded  所以注意：写递归需要递归出口