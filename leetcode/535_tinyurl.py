#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-24 23:23'

"""
TinyURL是一种URL简化服务， 
比如：
当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。
你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。

Python 3 解答
"""

import base64
import random


class Codec:

    db = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        flag = base64.encodebytes(longUrl.encode("utf-8"))
        flag = flag.decode("utf-8")
        flag = random.sample(flag, 6)
        flag = "".join(flag)
        self.db[flag] = longUrl
        return "https://tinyurl.com/{}".format(flag)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        flag = shortUrl.split("/")[-1]
        return self.db[flag]

if __name__ == '__main__':

# Your Codec object will be instantiated and called as such:

    urls = ["https://leetcode.com/problems/design-tinyurl", "https://leetcode.com/problems/design-test-tinyurl"]

    for url in urls:
        codec = Codec()
        print(codec.encode(url))
        print(codec.decode(codec.encode(url)))