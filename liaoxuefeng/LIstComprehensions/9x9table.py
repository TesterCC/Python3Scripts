#!/usr/bin/env python
# coding:utf-8

'''
Python输入 九九乘法表的各种方法
'''

# 9x9 table， 完整有重复
L5 = [("%d * %d = %d" % (m, n, m*n)) for m in range(1, 10) for n in range(1, 10)]
print(L5)
print("---------------------------------------")

# 一行输入九九乘法表，利用列表生产式，无格式整理,无重复
print([("%d * %d = %d" % (m, n, m*n)) for m in range(1, 10) for n in range(m, 10)])
print("---------------------------------------")

# 一行输入九九乘法表，带格式，无重复
print('\n'.join([("%d * %d = %d" % (m, n, m*n)) for m in range(1, 10) for n in range(m, 10)]))
print("---------------------------------------")
print("---------------------------------------")

# http://www.cnblogs.com/suiy-160428/p/5594389.html
# 1.长方形完整格式
for i in range(1, 10):
    for j in range(1, 10):
        print("%d*%d=%d" % (i, j, i*j), end=" ")
    print("")
print("---------------------------------------")

# 2.左上三角形
for i in range(1, 10):
    for j in range(i, 10):
        print("%d*%d=%d" % (i, j, i*j), end=" ")
    print("")

print("---------------------------------------")

# 3.右上三角形
#右上三角格式输出九九乘法表
for i in range(1,10):
    for k in range(1,i):
        print(end="       ")
    for j in range(i,10):
            print("%d*%d=%2d" % (i, j, i*j), end=" ")
    print("")

print("---------------------------------------")

# 4.左下三角形
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print("")

print("---------------------------------------")

# 5.右下三角形
for i in range(1,10):
    for k in range(1, 10-i):
        print(end="       ")
    for j in range(1, i+1):
        print("%d*%d=%2d" % (i, j, i*j), end=" ")
    print(" ")
