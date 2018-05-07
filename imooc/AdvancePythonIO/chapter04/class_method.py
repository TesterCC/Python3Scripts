#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/7 13:20'

"""
4-7 类方法、静态方法和实例方法
"""


class Date:

    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    def tomorrow(self):
        self.day += 1

    @staticmethod  # 因为在Date的命名空间中，所有调用时为Date.xxxx()
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        """
        检查年月日的有效性 －－ 忽略，实际开发绝对不能按这种方式来判断
        :param date_str:
        :return:
        """
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and (int(month) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) <= 31):
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date_str):  # cls代表类对象
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))


if __name__ == '__main__':
    new_day = Date(2018, 12, 24)
    print(new_day)
    new_day.tomorrow()
    print(new_day)

    print("---parse str---")
    # example 0
    date_str = "2018-12-31"
    year, month, day = tuple(date_str.split("-"))
    print(year, month, day)
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    print("--用staticmethod完成初始化--")
    # 用staticmethod完成初始化
    new_day = Date.parse_from_string(date_str)
    print(new_day)

    print("--用classmethod完成初始化--")
    # 用classmethod完成初始化
    new_day = Date.from_string(date_str)
    print(new_day)

    print("--vlid_str--")
    print(Date.valid_str("2018-12-32"))
    print(Date.valid_str("2018-12-24"))
