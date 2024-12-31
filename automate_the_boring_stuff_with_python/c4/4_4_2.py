#!/usr/bin/env python
# coding=utf-8

'''
Python编程快速上手
4.4.2_4.4.2
'''

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
print("-------------------")

spam2 = ['cat', 'dog', 'bat']
spam2.insert(1, 'chicken')
print(spam2)
print("-------------------")

# 4.4.3 remove()
spam3 = ['cat', 'bat', 'rat', 'elephant']
spam3.remove('bat')
print(spam3)
print("-------------------")

spam4 = ['cat', 'bat', 'rat', 'cat', 'dog', 'cat']
spam4.remove('cat')
print(spam4)