#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-09-30 01:57'

"""
2019 bilibili
https://www.nowcoder.com/practice/80ce674313ff43af9d7ac7a41ae21527?tpId=98&tqId=33025&tPage=11&rp=11&ru=/ta/2019test&qru=/ta/2019test/question-ranking

时间限制：1秒 空间限制：32768K

题目描述
从业 666 年的 BILIBILI 网络安全工程师 KindMo 最近很困惑，公司有一个业务总是受到 SSRF 攻击。请帮他写一个程序，判断输入的字符串是否属于内网IP，用于防御该漏洞。
我们知道常见的内网IP有，127.0.0.1，192.168.0.1 等。

输入描述:
每次输入仅包含一个IP字符串，即一个测试样例

输出描述:
对于每个测试实例输出整数1或0，
1代表True，即输入属于内网IP，
0代表False，即输入不属于内网IP或不是IP字符串。

示例1
输入
42.96.146.169

输出
0
"""


# 判断段首，不然累遍历肯定超内存限制啊
# 运行时间：30ms, 占用内存：3560k

def check_internal_ip(check_ip):

    check_ip_list = check_ip.split(".")
    if len(check_ip_list) == 4:
        a, b, c, d = check_ip_list

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if a > 255 or b > 255 or c > 255 or d > 255:
            return 0

        elif a == 10 and b >= 0 and c >= 0 and d >= 0:
            return 1

        elif a == 172 and (16 <= b <= 31) and c >= 0 and d >= 0:
            return 1

        elif a == 192 and b == 168 and c >= 0 and d >= 0:
            return 1

        else:
            return 0

    else:
        return 0


if __name__ == '__main__':
    check_ip = input()
    print(check_internal_ip(check_ip))
