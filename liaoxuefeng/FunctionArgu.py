# !/usr/bin/env python
# coding:utf-8

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000


def power1(x):
    return x * x


# print(power(3))
def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s

print(power1(3))
print(power(5, 2))
print(power(4))
print(power(5, 3))

# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
