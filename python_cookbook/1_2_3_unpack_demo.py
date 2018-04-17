#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/16 23:48'

"""
《Python+Cookbook》第三版中文v3.0.0
1.2 解压可迭代对象赋值给多个变量
P16
"""
# 星号解压语法在字符串操作的时候也会很有用,比如字符串的分割。

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

uname, *fields, homedir, sh = line.split(':')

print(uname, homedir, sh)
print(*fields)

print("---discard *---")
# 想解压一些元素后丢弃它们,你不能简单就使用*,但是你可以使用一个普通的废弃名称,比如_或者ign(ignore)。
record = ('ABCD', 50, 123.45, (12, 18, 2014))
name, *_, (*_, year) = record
print(name)
print(year)

print("---discard 2 *---")
name, weight, *ignore, (*ignore, date, year) = record
print(weight)
print(date)

print(">>>在很多函数式语言中,星号解压语法跟列表处理有许多相似之处。比如,如果你有 一个列表,你可以很容易的将它分割成前后两部分。")
items = [1, 3, 5, 7, 9, 2, 10]
head, *tail = items
print("head->{}".format(head))
print("tail->{}".format(tail))

print(">>>用这种分割语法去巧妙的实现递归算法")


def sums(items):
    head, *tail = items
    return head + sums(tail) if tail else head  # if tail exist, return head + sum(tail)


items = [1, 3, 5, 7, 9, 2, 10, 11]  # 48
print(sums(items))
