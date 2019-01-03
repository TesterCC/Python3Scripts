#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-12 10:32'

"""
此例未使用抽象类：精通Python设计模式 P8

代码并未禁止直接实例化
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
    return connector(filepath)

def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    # It isn't exist. cannot connect
    sqlite_factory = connect_to('data/inexistence.sq3')
    # print(sqlite_factory)
    print()

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data

    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format((len(liars))))

    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        # for p in liar.find('phoneNumber'):
        #     print('phone number ({})'.format(p.attrib['type']), p.text)
    print()

    json_factory = connect_to('data/goods.json')
    json_data = json_factory.parsed_data

    print('found: {} goods'.format(len(json_data)))
    for good in json_data:
        print('name: {}'.format(good['name']))
        print('price: {}'.format(good['ppu']))
        [print(list('topping:{}{}'.format(t['id'], t['type']) for t in good['topping']))]


if __name__ == '__main__':
    main()

