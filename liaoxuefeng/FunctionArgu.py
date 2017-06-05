# coding:utf-8
# !/usr/bin/env python
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
