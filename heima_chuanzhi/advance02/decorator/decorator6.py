# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/28 23:59'


"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    09-装饰器对有参数、无参数函数进行装饰
    5. 装饰器示例  例6：类装饰器（扩展，非重点）
    
    装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。
    在Python中一般callable对象都是函数，但也有例外。只要某个对象重写了 __call__() 方法，那么这个对象就是callable的。
"""

# 类装饰器demo


class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s" % func.__name__)
        self.__func = func

    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()


# 说明：
# 1. 当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
#    并且会把test这个函数名当做参数传递到__init__方法中
#    即在__init__方法中的func变量指向了test函数体
#
# 2. test函数相当于指向了用Test创建出来的实例对象
#
# 3. 当在使用test()进行调用时，就相当于让这个对象()，因此会调用这个对象的__call__方法
#
# 4. 为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法中就需要一个实例属性来保存这个函数体的引用
#    所以才有了self.__func = func这句代码，从而在调用__call__方法中能够调用到test之前的函数体

@Test
def test():
    print("----test---")


test()

# showpy()  #如果把这句话注释，重新运行程序，依然会看到"--初始化--"