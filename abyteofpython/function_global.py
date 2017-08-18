#!/usr/bin/env python
# coding=utf-8

# A Byte of Python -- P61 -- Python3

x = 50


def func():
    global x

    print("x is", x)
    x = 2
    print("Change global x to", x)

func()
print("Value of x is", x)