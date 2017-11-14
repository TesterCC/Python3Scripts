#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/13 22:54'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318650247930b1b21d7d3c64fe38c4b5a80d4469ad7000
访问限制
"""

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

# 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法
# 因为在方法中，可以对参数做检查，避免传入无效的参数
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score, please check it')

if __name__ == '__main__':
    bart = Student('Bart Simpson', 98)
    print(bart.get_name())
    print(bart.get_score())
    bart.set_score(63)
    print(bart.get_score())
    print(bart._Student__name)

# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名


