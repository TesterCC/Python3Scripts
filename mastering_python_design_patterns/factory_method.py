#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-12 10:32'

"""
此例未使用抽象类：精通Python设计模式 P8
"""

import xml.etree.ElementTree as etree
import json

class JSONConnector:
    def __init__(self, filepath):    # filepath包含文件名
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith(".json"):
        connector = JSONConnector
    elif filepath.endswith(".xml"):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))

def connect_to(filepath):
    pass