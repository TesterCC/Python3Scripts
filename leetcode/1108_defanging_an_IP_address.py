#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-10 13:58'

"""
easy
https://leetcode-cn.com/problems/defanging-an-ip-address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
"""


class Solution:
    # method 1
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

    # method 2

    def defangIPaddr_v2(self, address: str) -> str:
        import re
        pattern = re.compile(r'\.')
        return re.sub(pattern, "[.]", address)


if __name__ == '__main__':

    address = "127.0.0.1"

    so = Solution()
    print(so.defangIPaddr(address))
    print(so.defangIPaddr_v2(address))
