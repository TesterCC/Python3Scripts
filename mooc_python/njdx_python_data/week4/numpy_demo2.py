#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-05 13:52'

import numpy as np

from scipy import linalg

arr = np.array([[1,2],[3,4]])

print(linalg.det(arr))