# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/15 21:29'


"""
对INI文件应用场景，一般都是用于做初始化配置文件用，当然你要是愿意也可以用来做数据的存储。

留个小题目，请尝试自己用类封装一个通用的ini文件操作类。
"""

import configparser
import os


class ConfigINI:
    """
    用类封装一个通用的ini文件操作类
    """

    def __init__(self, filename):
        self.filename = filename
        self.config = None
        self.readhandle = None
        self.writehandle = None

    def get_ini(self):
        self.config = configparser.ConfigParser()
        try:
            self.readhandle = open(self.filename, 'r')
            self.writehandle = open(self.filename, 'a+')
        except Exception:
            print("Try load .ini file but FAILED, please check it.")
        return self.config

    def close_ini(self):
        if self.config:
            self.readhandle.close()
            self.writehandle.close()

    def get_value(self, section, option, default=""):
        try:
            value = self.config.get(section, option)
        except Exception:
            value = default
        return value

    def get_all_option(self):
        self.config.read(self.filename)
        # 获取它的所有section
        sections = self.config.sections()
        # 获取section下所有的options
        for sec in sections:
            options = self.config.options(sec)
            print(options)

    def get_all_data(self):
        # 下面开始我们来把刚才的ini文件读出来看看
        self.config.read(self.filename)
        # 获取它的所有section
        sections = self.config.sections()

        # 根据sections和options获取对应的value值
        for sec in sections:
            for option in self.config.options(sec):
                print("[%s] %s=%s " % (sec, option, self.config.get(sec, option)))


if __name__ == '__main__':
    ci = ConfigINI("config2.ini")
    ci.get_ini()

    print("获取所有options:")
    ci.get_all_option()

    print("获取所有Section-Option-Value：")
    ci.get_all_data()

    print("获取特定值：")
    r2 = ci.get_value("学习测试", "口号")
    print(r2)

    ci.close_ini()


