#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-30 13:17'

# 3-6
def coro():
    hello = yield 'hello'    # yield关键字在=右边作为表达式，可以被send值
    yield hello

c = coro()

# 输出'hello', 这里调用next产出第一个值'hello',之后函数暂停
print(next(c))

# 再次调用 send 发送值，此时hello变量赋值为'world'，然后yield产出hello变量的值 'world'
print(c.send('world'))

# 之后协程结束，后续再send值会抛异常StopIteration
# print(c.send('test'))