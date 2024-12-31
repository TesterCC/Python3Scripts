#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/9 15:14'

from configparser import ConfigParser
import os


class CustomINIParser:
    def __init__(self, path):
        self.path = path
        self.ini = ConfigParser()
        self.ini.read(self.path)

    # 获取sections列表
    def get_sections(self):
        if self.ini:
            return self.ini.sections()

            # 获取指定的section的options列表

    def get_options_by_section(self, section):
        if self.ini:
            return self.ini.options(section)

    # 获取指定section的配置信息列表
    def get_section_items(self, section):
        if self.ini:
            return self.ini.items(section)

    # 按类型读取配置信息

    # 返回字符串类型
    def get_string(self, section, option):
        if self.ini:
            return self.ini.get(section, option)

    # 返回int类型
    def get_int(self, section, option):
        if self.ini:
            return self.ini.getint(section, option)

    # 返回float类型
    def get_float(self, section, option):
        if self.ini:
            return self.ini.getfloat(section, option)

    # 返回bool类型    
    def get_boolean(self, section, option):
        if self.ini:
            return self.ini.getboolean(section, option)

    # 新增section
    def add_section(self, section):
        if self.ini:
            self.ini.add_section(section)
            self.ini.write(open(self.path, "w"))

    # 设置指定option值
    def set_option(self, section, option, value):
        if self.ini:
            self.ini.set(section, option, value)
            self.ini.write(open(self.path, "w"))

    # 删除指定section
    def remove_section(self, section):
        if self.ini:
            self.ini.remove_section(section)
            self.ini.write(open(self.path, "w"))

    # 删除指定option
    def remove_option(self, section, option):
        if self.ini:
            self.ini.remove_option(section, option)
            self.ini.write(open(self.path, "w"))     
