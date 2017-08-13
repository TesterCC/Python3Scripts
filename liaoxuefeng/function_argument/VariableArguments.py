#!/usr/bin/env python
# coding:utf-8

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000


'''

可变参数

在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

'''


# calc   a^2+b^2+...+n^2
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    print(sum)
    return sum


# 利用可变参数,改写calc()
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)
    return sum

nums = [1, 2, 3]     # list
nums_t = (1, 3, 5, 7)   # tuple    # print(type(nums_t))


if __name__ == '__main__':
    calc([1, 2, 3])
    calc([1, 3, 5, 7])
    print("---run calc2()---")
    calc2(1, 2)
    calc2()
    print("---传入list或tuple作为calc2()的参数---")
    calc2(nums[0], nums[1], nums[2])
    calc2(*nums)
    calc2(*nums_t)