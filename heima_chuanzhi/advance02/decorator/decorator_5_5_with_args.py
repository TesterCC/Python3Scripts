#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/27 11:59'


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
    
    例5:装饰器带参数,在原有装饰器的基础上，设置外部变量
    带有参数的装饰器，能够起到在运行时实现不同功能的作用
"""




from time import ctime
from time import sleep


def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s" % (func.__name__, ctime(), pre))
            if pre == "set":   # 利用参数pre做判断，执行不同功能
                print("参数是set")
            else:
                print("其他参数")
            return func()
        return wrappedfunc
    return timefun


# 1.先执行func_arg("set")函数,这个函数return的结果是func这个函数的引用
# 2.@timefun
# 3.使用@timefun对test进行装饰

@timefun_arg("set")    # --> return timefun
def foo():
    print("I am foo test.")


@timefun_arg("python")
def too():
    print("I am test, too.")


if __name__ == '__main__':
    foo()
    sleep(2)
    too()

