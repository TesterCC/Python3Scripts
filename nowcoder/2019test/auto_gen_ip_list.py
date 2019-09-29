#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-09-30 01:59'

"""
生成私有IP地址

私有IP地址范围：
A类：10.0.0.0-10.255.255.255
B类：172.16.0.0-172.31.255.255
C类：192.168.0.0-192.168.255.255

localhost：127.0.0.1

# A B 类型运行时间超慢，原因，看代码就能明白
"""


def generate_class_a_ip_list():
    # generate class A IP    # 16777216

    internal_list_a = []

    for i in range(256):
        for j in range(256):
            for k in range(256):
                internal_list_a.append("10.{}.{}.{}".format(i,j,k))
    return internal_list_a

def generate_class_b_ip_list():
    # generate class B IP   # 1048576
    internal_list_b = []

    for i in range(16,32):
        for j in range(256):
            for k in range(256):
                internal_list_b.append("172.{}.{}.{}".format(i,j,k))
    return internal_list_b


def generate_class_c_ip_list():
    # generate class C IP   # 65536
    internal_list_c = []
    for i in range(256):
        for j in range(256):
            internal_list_c.append("192.168.{}.{}".format(i,j))
    return internal_list_c


def generate_all_lan_ip_list():
    # generate all lan ip   # 17891329
    internal_list_local = ['127.0.0.1']

    all_lan_ip_list = internal_list_local + generate_class_a_ip_list() + generate_class_b_ip_list() + generate_class_c_ip_list()

    return all_lan_ip_list

if __name__ == '__main__':
    generate_all_lan_ip_list()