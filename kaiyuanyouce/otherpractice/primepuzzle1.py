#!/usr/bin/python env
# coding:utf-8

'''
判断3-200000之间又多少个素数，并输出所有素数
'''

import time

from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


start_time = time.time()
nums = list(filter(is_prime, range(3, 200000)))
end_time = time.time()

elapsed_time = end_time - start_time

print(nums)
print(len(nums))
print(elapsed_time)

