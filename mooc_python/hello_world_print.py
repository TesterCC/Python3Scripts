#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-21 22:03'

TmpStr = input("")
if eval(TmpStr) == 0:
    print("Hello World")
elif eval(TmpStr) > 0:
    st = ''
    string = "Hello World"
    for i in range(len("Hello World")):

        if (i + 1) % 2 != 0:
            st = st + string[i];
            if len(string) == (i + 1):
                print(st);
        else:
            st = st + string[i]
            print(st)
            st = ''
elif eval(TmpStr) < 0:
    for ch in "Hello World":
        print(ch)
else:
    print("")