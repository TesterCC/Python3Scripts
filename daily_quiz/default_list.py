# -*- coding: utf-8 -*-
# @Time    : 2022/9/2
# @Author  : SecCodeCat

# Python只在函数第一次被评估时初始化默认参数
# It set default values for both parameters as empty lists. This is a super reasonable thing to do! However, Python only initializes default parameters when the function is first evaluated, which means that the same list is used for every call to the function.
def f(L=[]):
    L.append(1)
    print(L)


def f_other(B=False):
    print(B)


if __name__ == '__main__':
    print("test list args:")
    f()
    f()
    f()
    print("test boolean args:")
    f_other()
    f_other(True)
    f_other()
