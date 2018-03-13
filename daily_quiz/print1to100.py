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


if __name__ == '__main__':

    print(List)