# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/29 22:47'


"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    14-python动态添加属性以及方法   
        4. 运行的过程中给类绑定(添加)方法
    15-types.MethodType的作用
"""

import types     # 动态添加属性需要


class Person:
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("---%s正在吃---" % self.name)


def run(self):
        print("---%s正在跑---" % self.name)


# 添加静态方法
@staticmethod
def stest():
    print("---- static method ----")


# 添加类方法
@classmethod
def printNum(cls):
    print("--- class method ---")


if __name__ == '__main__':
    p1 = Person("p1", 10)
    p1.eat()

    # p1.run = run
    # p1.run()
    # 虽然p1对象中run属性已经指向23行的函数，但这句代码还不对
    # 因为run属性指向函数，是后来添加的，即p1.run()的时候，并没有把p1当作第1个参数
    # 导致了第23行的函数调用的时候，出现了缺少参数的问题。

    print("运行的过程中给类绑定(添加)方法示例:")
    # 正确的添加方式：types.MethodType(func_name, obj)
    # 运行的过程中给实例绑定(添加)方法
    p1.run = types.MethodType(run, p1)
    p1.run()

    print("xxxx")
    # types.MethodType的作用
    xxxx = types.MethodType(run, p1)
    xxxx()

    print("添加静态方法:")
    # 给类添加一个属性并指向静态方法
    Person.test = stest
    Person.test()

    Person.xxx = stest
    Person.xxx()

    # 实例也能使用这个绑定的静态方法
    p1.xxx()


    print("添加类方法:")
    Person.printNum = printNum
    Person.printNum()
    p1.printNum()

    print("dir(p1): ")
    print(dir(p1))


