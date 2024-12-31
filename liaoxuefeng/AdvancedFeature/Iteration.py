#!/usr/bin/env python
# coding:utf-8

# 迭代 Iteration
# https://note.youdao.com/web/#/file/WEBe4c9e8cbc7e3e55236eef83005303584/note/WEBde782af9e31fda2d1a63177b48a43542/

from collections import Iterable


d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)     # 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

print("----------------------------")

# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()
for value in d.values():
    print(value)

print("----------------------------")

# 如果要同时迭代key和value，可以用for k, v in d.items()。
for k, v in d.items():
    print(k, "-->", v)

print("----------------------------")
# 由于字符串也是可迭代对象，因此，也可以作用于for循环
for ch in 'ABCD':
    print(ch)

print("----------------------------")
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable))   # str是否可迭代
print(isinstance([1, 2, 3], Iterable))   # list是否可迭代
print(isinstance(123, Iterable))   # int是否可迭代
print(isinstance((1, 2, 3, 4), Iterable))   # tuple是否可迭代

print("----------------------------")
# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, v in enumerate(['A', 'B', 'C']):
    print(i, "->", v)

# for循环里，同时引用了两个变量，在Python里是很常见的
for x,y in [(1,1), (2,4), (3,9)]:
    print("x=", x, "y=", y)


