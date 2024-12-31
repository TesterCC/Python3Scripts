#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-03 17:03'

"""
Python 实现精确的四舍五入
https://zhuanlan.zhihu.com/p/60952919
https://docs.python.org/zh-cn/3/library/decimal.html#decimal.Decimal.quantize

OUND_HALF_EVEN实际上就是奇进偶舍
如果要指定真正的四舍五入，那么我们需要在quantize中指定进位方式为ROUND_HALF_UP


如果你传入的参数为浮点数，并且这个浮点值在计算机里面不能被精确存储，那么它会先被转换为一个不精确的二进制值，然后再把这个不精确的二进制值转换为等效的十进制值。

对于不能精确表示的小数，当你传入的时候，Python在拿到这个数前，这个数就已经被转成了一个不精确的数了。

但是如果你传入的是字符串'11.245'，那么Python拿到它的时候，就能知道这是11.245，不会提前被转换为一个不精确的值。

所以，建议给Decimal的第一个参数传入字符串型的浮点数，而不是直接写浮点数。
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext

print(getcontext().rounding)

origin_num = Decimal('11.245')
answer_num = origin_num.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
print(answer_num)   # 四舍五入，没有失去精度