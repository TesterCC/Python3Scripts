#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/3/13 23:44'


"""
每日一题 2018年3月12日

1. 遍历并打印0到100
2. 如果数字能被3整除，显示Fizz；如果数字能被5整除，显示Buzz；
如果能同时被3和5整除，就显示FizzBuzz

结果应该类似：0,1,2，Fizz，4，Buzz，6……14，FizzBuzz，16……

"""
# 注意点，考虑到0
# 初级解法
List = []

for i in range(0, 101):
    if i == 0:
        List.append(i)
    elif i % 3 == 0:
        List.append("Fizz")
    elif i % 5 == 0:
        List.append("Buzz")
    elif i % 3 == 0 and i % 5 ==0:
        List.append("FizzBuzz")
    else:
        List.append(i)


# 中级解法
def printList(i):
    if i == 0:
        return i
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    elif i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    else:
        return i


# 看似高大上解法 use numpy,其实和第二种基本一致
def numdiv(i):
    if i == 0:
        return i
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    elif i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    else:
        return i


if __name__ == '__main__':

    print(List)

    print("-"*70)

    tList = [i for i in range(101)]
    print(list(map(printList, tList)))

    print("-" * 70)

    import numpy as np
    print(list(map(numdiv, np.arange(101))))