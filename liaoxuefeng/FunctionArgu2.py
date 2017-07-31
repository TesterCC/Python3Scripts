# !/usr/bin/env python
# coding:utf-8


# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    print('------------------')

if __name__ == '__main__':
    print(enroll('Lily', 'F'))
    print(enroll('Tom', 'M', city='Shenzhen'))
    print(enroll('Eric', 'M', 20))

# 默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。
