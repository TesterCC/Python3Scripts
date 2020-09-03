# coding=utf-8
'''
DATE: 2020/09/03
AUTHOR: Yanxi Li
'''

"""
1.11 命名切片

问题：
你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。

解决方案1：命名切片

内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方
"""

record = '..........100...........513.25...........'

# 内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方

SHARES = slice(10, 13)

PRICE = slice(24, 30)

cost = int(record[SHARES]) * float(record[PRICE])

print(record[SHARES])
print(record[PRICE])

print(cost)

print("="*18 + "demo2" + "="*18)

# 如果你有一个切片对象 a，你可以分别调用它的 a.start, a.stop, a.step 属性来获取更多的信息.

a = slice(5, 50, 3)

print(a.start)
print(a.stop)
print(a.step)
