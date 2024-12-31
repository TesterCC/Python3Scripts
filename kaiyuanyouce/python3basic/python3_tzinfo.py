# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/17 01:16'


from datetime import datetime
from datetime import tzinfo
from datetime import timedelta


"""
tzinfo是关于时区信息的类
tzinfo是一个抽象类，所以不能直接被实例化
"""


class UTC(tzinfo):
    """UTC"""
    def __init__(self, offset=0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return timedelta(hours=self._offset)


if __name__ == '__main__':

    #北京时间
    beijing = datetime(2018, 11, 11, 0, 0, 0, tzinfo=UTC(8))

    #曼谷时间
    bangkok = datetime(2018, 11, 11, 0, 0, 0, tzinfo=UTC(7))

    #北京时间转成曼谷时间
    print(beijing.astimezone(UTC(7)))

    #计算时间差时也会考虑时区的问题
    timespan = beijing - bangkok
    print(timespan)