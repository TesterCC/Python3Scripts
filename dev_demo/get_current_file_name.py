# -*- coding:utf-8 -*-


import sys

import os

print("-" * 33)
# abs path
print(__file__)
print(sys.argv[0])

# relative path
print(os.path.basename(__file__))
print(os.path.basename(sys.argv[0]))
