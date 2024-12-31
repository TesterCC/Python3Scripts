#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/14 15:15'

"""
https://pypi.org/project/Cerberus/
"""

from cerberus import Validator

v = Validator({'name': {'type': 'string', "required": True}})

print(v.validate({'name': 'Lily'}))
print(v.validate({'name': 33}))

