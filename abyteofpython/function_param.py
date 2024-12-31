#!/usr/bin/env python
# coding=utf-8

# A Byte of Python -- P59 -- Python3


def print_max(a, b):
    if a > b:
        print(a, ' is maximum')
    elif a == b:
        print(a, ' is equal to', b)
    else:
        print(b, ' is maximum')


if __name__ == '__main__':

    # 直接传递字面值
    print_max(3, 4)

    x = 5
    y = 7
    # 以参数的形式传递变量
    print_max(x, y)