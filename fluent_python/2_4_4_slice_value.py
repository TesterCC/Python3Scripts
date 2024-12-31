# coding=utf-8
'''
DATE: 2020/09/03
AUTHOR: Yanxi Li
'''

# 2.4.4

l = list(range(10))

print(l)

l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)

l[3::2] = [11, 22]
print(l)

# l[2:5] = 100
# print(l)  #  TypeError: can only assign an iterable

l[2:5] = [100]
print(l)
