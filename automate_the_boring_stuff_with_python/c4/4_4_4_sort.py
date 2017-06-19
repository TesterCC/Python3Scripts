#!/usr/bin/env python
# coding=utf-8

'''
Python编程快速上手
4.4.4
'''


spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam.sort(reverse=True)
print("Reverse: ")
print(spam)
print("------------------------")


# 使用ASCII字符顺序 大写字母排在小写字母之前
spam2 = ['ants', 'cats', 'dogs', 'badgers', 'bats', 'elephants', 'zebras']
spam2.sort()
print(spam2)
spam2.sort(reverse=True)
print("Reverse: ")
print(spam2)
print("------------------------")


# 若想按照普通字典顺序来排，使用sort()时要设置key=str.lower
spam3 = ['a', 'z', 'A', 'Z']
spam3.sort(key=str.lower)
print(spam3)