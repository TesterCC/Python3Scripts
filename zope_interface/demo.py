#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/2 22:57'

# normal example

class Host(object):

    def goodmorning(self, name):
        """ Say good morning to guests """
        return "Good morning, %s!" % name


if __name__ == '__main__':
    h = Host()
    hi = h.goodmorning('zhangsan')
    print(hi)