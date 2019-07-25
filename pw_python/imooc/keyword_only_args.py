#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-25 15:38'

# Feature: Keyword only arguments

def add(a,b,*,c,d):
    return a+b+c

# print(add(1,2,3,4))   # error
print(add(1,2,c=3,d=4))   # correct
