#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-14 14:25'

"""
4-1 Python内置数据结构算法常考

Python dict底层结构

dict底层使用的哈希表（Hashtable）：
（为什么使用哈希表?）
1.为了支持快速查找，故使用了哈希表作为底层结构。
(set在cpython解释器的实现用了hashtable,所以效率奇高)

2.哈希表平均查找时间复杂度O(1)。

3.CPython解释器使用二次探查解决哈希冲突问题。

面试常问hastable的底层原理和实现细节问题：
哈希表冲突和扩容

1)哈希表是如何解决hash冲突的？ 比如常见的：链接法 和 探查法（线性探查、二次探查）
2)哈希表是如何扩容的？  数组，如何扩容
"""

"""
Python list/tuple 的区别

list vs tuple

共同点：都是线性结构，支持下标访问

区别：
1.list是可变对象，tuple保存的引用不可变
2.list没法作为字典的key（可变对象不可hash），tuple可以    

保存的引用不可变值得是：
你没法替换掉这个对象，但是如果对方本身是一个可变对象，是可以修改这个引用指向的可变对象的。
"""

# 举例说明：tuple保存的引用不可变

t = ([1],2,3)

print(t)

# t[1] = 3  # report error

t[0].append(1)

print(t)