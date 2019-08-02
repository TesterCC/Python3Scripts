#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-02 15:14'


rest2fun = {
    "no_offer": lambda: print("XXX公司 反正XXX都要走了"),
    "offer": lambda: print("可以的，YY很棒，公司还不算眼拙")
}

if __name__ == '__main__':
    # rest2fun["offer"]()    <function __main__.<lambda>()>
    rest2fun["offer"]()
    rest2fun["no_offer"]()