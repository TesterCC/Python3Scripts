#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-01 10:18'

"""
REF：https://www.cnblogs.com/shenbuer/p/7724091.html

方法三、使用python的装饰器（decorator）实现单例模式，这是一种更Pythonic的方法；
单例类本身的代码不是单例的，通过装饰器使其单例化
"""

def singleton(cls):
    '''定义一个装饰器，它返回了一个内部函数getinstance(),该函数会判断某个类是否在字典instances中。
    如果不存在，则会将cls作为key，将cls(*args, **kw)作为value存到instances中，否则，直接返回instances[cls]。
    '''
    instances = {}
    def getinstance(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return getinstance


class Hello(object):
    """
    Python2程序员经常犯的一个错误是，只重写了__eq__()，而没有重写__ne__()方法，导致不可预计的错误。
    而Python3会自动重写__ne__()，如果你没有重写的话。
    """
    def __eq__(self, other):
        return (self.__class__ == other.__class__)

# 下面的代码不可改变
h1 = Hello()
h2 = Hello()

print(h1 == h2)
print(h1 is h2)    # is比较是否引用自同一个对象


# use decorator
@singleton
class MySingle:
    pass

s1 = MySingle()
s2 = MySingle()
print(s1 == s2)  # 注意！！！ 重写__eq__只是改变了 == 的结果，
print(s1 is s2)


"""
单例模式总结：

内容：
    保证一个类只有一个实例，并提供一个访问它的全局访问点。

适用场景：
    当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时

优点：
    对唯一实例的受控访问
    单例相当于全局变量，但防止了命名空间被污染

与单例模式功能相似的概念：全局变量、静态变量（方法）
"""
