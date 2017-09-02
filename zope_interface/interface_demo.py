#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/2 22:59'


from zope.interface import Interface
from zope.interface.declarations import implementer

# interface example
# define interface


class IHost(Interface):
    def goodmorning(self, host):
        """ Say good morning to host """


@implementer(IHost)
class Host:
    def goodmorning(self, guest):
        """ Say good morning to guest """
        return "Good morning, %s!" % guest


@implementer(IHost)
class Reject:
    def goodmorning(self, guest):
        """ Say good morning to guest """
        return "Don't say good morning, %s!" % guest


if __name__ == '__main__':
    p = Host()
    hi = p.goodmorning("Tom")
    print(hi)

    print("--------------------------")

    p2 = Reject()
    nohi = p2.goodmorning("Jim")
    print(nohi)
