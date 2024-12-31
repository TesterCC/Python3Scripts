# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/22 17:41'


"""
03 算法
   03.Python列表和字典
     02-Python列表类型不同操作的时间效率
     pop操作测试
     
Python List pop()方法
函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
"""

from timeit import Timer


x = list(range(700000))


pop_zero = Timer("x.pop(0)", "from __main__ import x")
print("pop_zero ", pop_zero.timeit(number=1000), "seconds")

pop_end = Timer("x.pop()", "from __main__ import x")
print("pop_end ", pop_end.timeit(number=1000), "seconds")

# 测试pop操作：从结果可以看出，pop最后一个元素的效率远远高于pop第一个元素