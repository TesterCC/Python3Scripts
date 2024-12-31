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


# 例1:无参数的函数

def timefun(func):
    def wrappedfunc():
        # 4 内部函数wrappedfunc被引用，所以外部函数的func变量(自由变量)并没有释放
        print("%s called at %s" % (func.__name__, ctime()))
        func()  # 5 func里保存的是原foo函数对象
    return wrappedfunc


@timefun    # 2 foo先作为参数赋值给func后,foo接收指向timefun返回的wrappedfunc
def foo():   # 1 foo = timefun(foo)
    print("I am a test foo.")


if __name__ == '__main__':
    foo()   # 3 调用foo(),即等价调用wrappedfunc()
    sleep(2)
    foo()
