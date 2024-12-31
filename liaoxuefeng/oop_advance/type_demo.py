#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/17 11:37'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
使用元类
type()
"""


class Hello1(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello1()
print(h.hello())
print(h.hello('test'))

# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type
print(type(Hello1))

# 而h是一个实例，它的类型就是class Hello。
print(type(h))

print("------------")
# 可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义


def fn(self, name='world'):   # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
he = Hello()
he.hello()

print(type(Hello))
print(type(he))

# 要创建一个class对象，type()函数依次传入3个参数：
#
# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

# 动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。