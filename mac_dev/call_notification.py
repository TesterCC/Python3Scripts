#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-02-14 23:10'

"""
Python在Mac下的优雅提示方式
https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel
https://www.zhihu.com/question/48885992
"""

from subprocess import call

cmd = 'display notification "Lorem ipsum dolor sit amet" with title "Title TEST"'

call(["osascript", "-e", cmd])