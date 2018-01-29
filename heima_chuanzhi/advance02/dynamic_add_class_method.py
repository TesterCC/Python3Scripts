# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/29 22:47'


"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    14-python动态添加属性以及方法
        4. 运行的过程中给类绑定(添加)方法
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


if __name__ == '__main__':
    p1 = Person("p1", 10)
    p1.eat()

    # p1.run = run
    # p1.run()
    # 虽然p1对象中run属性已经指向23行的函数，但这句代码还不对
    # 因为run属性指向函数，是后来添加的，即p1.run()的时候，并没有把p1当作第1个参数
    # 导致了第23行的函数调用的时候，出现了缺少参数的问题。

    print("运行的过程中给类绑定(添加)方法示例:")
    # 正确的添加方式：types.MethodType()
    # 运行的过程中给类绑定(添加)方法
    p1.run = types.MethodType(run, p1)
    p1.run()






