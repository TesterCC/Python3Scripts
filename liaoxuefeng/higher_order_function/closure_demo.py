#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/12 22:57'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000
闭包
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
"""


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

print("-------------")

# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))    # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count2()

print(f1())
print(f2())
print(f3())

# 缺点是代码较长，可利用lambda函数缩短代码。