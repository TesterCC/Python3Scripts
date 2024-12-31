# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/25 22:42'


"""
装饰器(decorator)功能

1.引入日志
2.函数执行时间统计
3.执行函数前预备处理
4.执行函数后清理功能
5.权限校验等场景
6.缓存

01.python高级1
  02.python高级2-生成器、闭包、装饰器
    09-装饰器对有参数、无参数函数进行装饰
    5. 装饰器示例   
"""

from time import ctime
from time import sleep


# 例4:装饰器中的return
# 一般情况下为了让装饰器更通用，可以有return

def timefun(func):
    def wrappedfunc():
        print("%s called at %s" % (func.__name__, ctime()))
        re = func()   # 保存返回的'----hahaha---'
        return re     # 把hahaha返回到52行调用
    return wrappedfunc


@timefun
def foo():
    print("I am foo test")


@timefun
def getInfo():
    return '----hahaha---'


if __name__ == '__main__':

    foo()
    sleep(2)
    foo()

    print(getInfo())
