#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/13 17:15'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000#0

请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
"""
from functools import wraps


def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if(isinstance(text, str)):
                print('%s: call %s()' % (text, func.__name__))
            else:
                print('call %s()' % text.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator if(isinstance(text, str)) else decorator(text)


@log
def now():
    print('2017')

@log("test2")
def now2():
    print('2017-2')

# print(now.__name__)
print(now())

# print(now2.__name__)
print(now2())


# 要点：
# (isinstance(text,str))  若是加字符串的话返回函数名称：
# 调用执行为：log(text)(func)=>decorator(func)=>wrapper备用
# 若不是字符串的话直接执行decorator(text)其中text即func
# 调用执行为：log(func)(func)=>decorator(func)=>wrapper用,实只有log的时候就直接执行的decorator(func)







