# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/8 10:19'

"""
https://docs.python.org/3/library/urllib.robotparser.html
"""

import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()

rp.set_url("https://arstechnica.com/robots.txt")

rp.read()
print(rp.read())

j1 = rp.can_fetch('*', 'http://arstechnica.com/')
print(j1)

j2 = rp.can_fetch('*', 'http://arstechnica.com/cgi-bin/')
print(j2)

