#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/26 23:34'


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

# 使用通用的装饰器完成对函数进行装饰


def func(functionName):
    """
    使用通用的装饰器完成对函数进行装饰
    """
    def func_in(*args, **kwargs):
        print("---记录日志---")
        ret = functionName(*args, **kwargs)
        return ret
    return func_in


@func
def ftest():
    print("---test---")
    return "haha"


@func
def ftest2():
    print("---test2---")


@func
def ftest3(a):
    print("---test3---a=%d" % a)


ret = ftest()
print("ftest return value is %s" % ret)

a = ftest2()
print("test2 return value is %s" % a)


ftest3(11)