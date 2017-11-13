#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/13 17:37'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143184474383175eeea92a8b0439fab7b392a8a32f8fa000
偏函数
"""

# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
r0 = int('12345')
print(r0)

# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
r1 = int('12345', base=8)
print(r1)

r2 = int('12345', 16)
print(r2)


print('-----Test int2()-----')
# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
# 于是，可以定义一个int2()的函数，默认把base=2传进去

def int2(x, base=2):
    return int(x, base)

r3 = int2('1000000')
print(r3)

r4 = int2('1010101')
print(r4)


print('-----Test int22() partial function-----')
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int22

import functools

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
int22 = functools.partial(int, base=2)    # how to use   这里实际上固定了int()函数的关键字参数base

r5 = int22('1000000')
print(r5)

r6 = int22('1010101')
print(r6)

# 注意到上面的新的int22函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值

r7 = int22('1000000', base=10)
print(r7)


print("-----Test max2()-----")

max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边
# 也就是：max2(5, 6, 7)
# 相当于：args = (10, 5, 6, 7)
# max(*args)

r8 = max2(5, 6, 7)
print(r8)

r9 = max2(5, 6, 7, 20)
print(r9)

