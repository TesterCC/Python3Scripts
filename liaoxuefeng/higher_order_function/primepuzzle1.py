#!/usr/bin/python env
# coding:utf-8

'''
判断3-2000之间又多少个素数，并输出所有素数
'''


def is_prime(num):
    for i in (2, num):
        if num % i == 0:
            return False
        return True


nums = list(filter(is_prime, range(3, 20)))
print(nums)
print(len(nums))
