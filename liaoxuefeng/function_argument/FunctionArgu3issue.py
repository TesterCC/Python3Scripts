#!/usr/bin/env python
# coding:utf-8

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000
# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑
# 定义默认参数要牢记一点：默认参数必须指向不变对象


def add_end(L=[]):
    L.append('END')
    print(L)
    return L


def add_end_r(L=None):
    if L is None:
        L = []
    L.append('END')
    print(L)
    return L



if __name__ == '__main__':
    add_end([1, 2, 3])
    add_end(['x', 'y', 'z'])
    add_end()
    add_end()  # add 'END'
    add_end()  # add 'END'

    print("-------fix bug: use add_end_r()--------")

    add_end_r([1, 2, 3])
    add_end_r(['x', 'y', 'z'])
    add_end_r()
    add_end_r()  # add 'END'


    '''
    原因解释如下：
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
定义默认参数要牢记一点：默认参数必须指向不变对象
    '''

