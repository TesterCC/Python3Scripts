#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-11 16:47'

dayfactor = 0.01
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)

print("Day Up : {:.2f}, Day Down {:.2f}".format(dayup, daydown))