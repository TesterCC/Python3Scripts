# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/14 02:29'


"""
看两个for语句实现九九乘法表
"""


def print_table():
    """
    nested loop
    """
    print(u"九九乘法表：")
    for i in range(1, 10):
        for j in range(i, 10):
            print(u"%d x %d = %2d" % (i, j, i * j), end="    ")
        print("")


def sum_list():
    """
    用while循环语句来计算0-100所有的偶数和
    """
    print(u"计算0-100间所有偶数和:")

    n = 100
    index = 0
    sum = 0
    while index <= n:
        sum += index
        index += 2

    print(u"0-100间偶数和= %d " % sum)


def print_table2():
    """
    用while和for结合一起尝试实现一个九九乘法表
    """
    print(u"九九乘法表实例：")
    n = 1
    while n <= 9:
        for m in range(n, 10):
            print(u"%d * %d = %2d" % (n, m, n * m), end="  ")
        print("")
        n = n + 1


def break_test():
    n = 0
    while n <= 3:
        for j in range(4):
            while j == 2:
                print("print and exit current while loop.")
                break
                print("Test 1234")
            print("n-->%d, j-->%d" % (n, j))
        n += 1


if __name__ == '__main__':
    print_table()
    sum_list()
    print_table2()
    break_test()