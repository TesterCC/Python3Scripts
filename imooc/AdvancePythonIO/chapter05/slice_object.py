#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/14 14:06'


class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        pass

    def __getitem__(self, item):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self, item):
        pass


if __name__ == '__main__':
    staffs = ["Jack", "Alice", "Bob", "Mary", "Tom"]
    group = Group(company_name="fspt", group_name='user', staffs=staffs)
    print(group[:2])     # None
