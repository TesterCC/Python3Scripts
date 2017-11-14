#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/14 19:44'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431865288798deef438d865e4c2985acff7e9fad15e3000
继承和多态
多态（polymorphism）

在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）。
"""


class Animal(object):
    def run(self):
        print('Animal is running ...')


# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
class Dog(Animal):
    # 也可以对子类增加一些方法，比如Dog类
    def run(self):
        print('Dog is running ...')

    def eat(self):
        print('Eating meat ...')


class Cat(Animal):
    def run(self):
        print('Cat is running ...')

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个好处：多态。


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


# 对于Python这样的动态语言来说，则不一定需要传入Animal类型
class Timer(object):
    def run(self):
        print('Start...')


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()

    # 判断一个变量是否是某个类型可以用isinstance()判断
    print(isinstance(dog, Dog))
    print(isinstance(cat, list))
    print(isinstance(cat, Animal))

    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())
    run_twice(Tortoise())
    run_twice(Timer())
