# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/31 05:32'


"""
04 无法绕过的json解析
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484112&idx=1&sn=b6cd8c2c4190561d92f85a966d86516e&scene=19#wechat_redirect
"""

import json


def python_json():
    """
    实例演示的都是在内存中进行
    将python对象转化存json串
    """
    print("python json串格式化实例:")

    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    print(type(data))
    print(isinstance(data, list))

    json_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

    # 打印格式化的json串
    print(json_data)
    print(type(json_data))
    print(isinstance(json_data, str))


if __name__ == '__main__':
    python_json()


