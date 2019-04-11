#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-11 16:47'

dayup = pow(1.001, 365)
daydown = pow(0.999, 365)

print("Day Up : {:.2f}, Day Down {:.2f}".format(dayup, daydown))