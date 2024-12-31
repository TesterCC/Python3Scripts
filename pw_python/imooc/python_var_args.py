#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-22 14:35'


# What's args?
def print_multiple_args(*args):
    print(type(args), args)
    for idx, val in enumerate(args):
        print(idx, val)

print_multiple_args()
print("-"*40)
print_multiple_args("a")
print("-"*40)
print_multiple_args("a", "b")
print("-"*40)
print_multiple_args("a", "b", "c")
print("~"*40)
print_multiple_args(*["a", "b", "c"])  # 传入一个列表

print("*"*60)

# What's kwargs?
def print_kwargs(**kwargs):
    print(type(kwargs), kwargs)
    for k,v in kwargs.items():
        print(f'{k}:{v}')

print_kwargs()
print("-"*40)
print_kwargs(a=1)
print("-"*40)
print_kwargs(a=1, b=2)
print("~"*40)
print_kwargs(**dict(a=1, b=2))   # 传入一个字典

print("*"*60)

# print all
def print_all(a, *args, **kwargs):
    print(a)
    if args:
        print(f'args: {args}')
    if kwargs:
        print(f'kwargs: {kwargs}')

print_all('I', 'love' , name='python')
print("-"*40)
print_all('I', 'love', 'code' , name='python')