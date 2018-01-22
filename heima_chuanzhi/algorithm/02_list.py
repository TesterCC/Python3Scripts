# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/22 16:23'

"""
03 算法
   03.Python列表和字典
     02-Python列表类型不同操作的时间效率
Python内置类型性能分析
timeit模块可以用来测试一小段Python代码的执行速度

list的操作测试
"""


def t1():
    """
    append空列表添加元素 从队尾添加
    """
    li = []
    for i in range(10000):
        li.append(i)


def t2():
    """
    +=直接添加元素
    """
    li = []
    for i in range(10000):
        li += [i]


def t3():
    """
    使用列表生成器
    """
    li = [i for i in range(10000)]


def t4():
    """
    使用list()转换 --> 最快
    """
    li = list(range(10000))


def t5():
    """
    利用list extend()来扩展列表
    """
    li = []
    for i in range(10000):
        li.extend([i])    # 和extend 接近


def t6():
    """
    利用list insert()来扩展列表 从队头添加
    """
    li = []
    for i in range(10000):
        li.insert(0, i)


def t7():
    """
    list + [i]直接添加元素
    """
    li = []
    for i in range(10000):
        li = li + [i]


from timeit import Timer


timer1 = Timer("t1()", "from __main__ import t1")
print("t1 list append():", timer1.timeit(1000))

timer2 = Timer("t2()", "from __main__ import t2")
print("t2 += :", timer2.timeit(1000))

timer3 = Timer("t3()", "from __main__ import t3")
print("t3 [i for i in range]:", timer3.timeit(1000))

# timer4 最快
timer4 = Timer("t4()", "from __main__ import t4")
print("t4 list(range()):", timer4.timeit(1000))

timer5 = Timer("t5()", "from __main__ import t5")
print("t5 list extend():", timer5.timeit(1000))

# 28s 向对列头部添加最慢，因为是由列表的数据存储方式决定。
timer6 = Timer("t6()", "from __main__ import t6")
print("t6 list insert():", timer6.timeit(1000))

# list = list + [i]直接添加元素
timer7 = Timer("t7()", "from __main__ import t7")
print("t7 list = list + [i]:", timer7.timeit(1000))

