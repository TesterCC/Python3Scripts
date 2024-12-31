# -*- coding:utf-8 -*-

"""
实现一个四则运算的类, 要求实现任意两个数的加减乘除运算
"""


class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        """加法"""
        return self.a + self.b

    def sub(self):
        """减法"""
        return self.a - self.b

    def mul(self):
        """乘法"""
        return self.a * self.b

    def div(self):
        """除法"""
        if self.b != 0:
            # 保留小数点后2位
            return round(self.a / self.b, 2)
        raise ("除数为0，非法数值，请更正")