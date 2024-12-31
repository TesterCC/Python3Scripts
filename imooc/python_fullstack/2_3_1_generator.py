#!/usr/bin/env python
# coding=utf-8

# Python 全栈案例初体验  2-3
# http://www.imooc.com/video/15369

a = range(1, 11)

b = [i for i in a]

print("a's type is %s" % type(a))
print("b's type is %s" % type(b))

print(list(b))