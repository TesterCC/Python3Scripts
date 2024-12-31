# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/17 01:20'


"""
对于json的解析，简而言之，就是将其转换成字典，在python中对字典进行操作
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484057&idx=1&sn=911727b52e35735765a1fdbeac8b34b1&scene=19#wechat_redirect
"""

import json


def json2dict(json_str):
    """
    json串转dict（字典）示例
    """
    print("json转dict示例:")

    # 原类型
    print("原类型：", type(json_str))

    # 转成dict对象
    # 会被转换成字典类型
    json_dict = json.loads(json_str)
    print("转换后的类型：", type(json_dict))
    return json_dict


def dict2json(json_dict):
    """
    dict字典转json串示例
    """
    print("dict字典转json串示例:")
    print("原类型：", type(json_dict))

    # 将字典转换成json串
    # 会被转换成字符串类型
    json_str = json.dumps(json_dict)

    print("转换后的类型：", type(json_str))
    print(json_str)

    return json_str


if __name__ == '__main__':

    # json to dict
    json_str1 = '{"name": "开源优测", "url": "www.testingunion.com", "id": "DeepTest"}'

    d = json2dict(json_str1)

    # 遍历字典
    for (k, v) in d.items():
        print(k, " : ", v)

    print("-" * 70)

    # dict to json
    json_dict1 = {
        "name": "开源优测",
        "url": "www.testingunion.com",
        "id": "DeepTest"
    }

    r = dict2json(json_dict1)

    print("-" * 70)

    print("json串解析高级实例")
    json_demo = """
            {
                "weixin": [
                    {
                        "name": "开源优测",
                        "uid": "DeepTest",
                        "desc": "分享开源测试技术"
                    },
                    {
                        "name": "开源优测_demo",
                        "uid": "DeepTest_demo",
                        "desc": "分享开源测试技术_demo"
                    }
                ],
                "web": [
                    {
                        "url": "www.testingunion.com",
                        "name": "开源优测社区",
                        "desc": "分享各类开源测试技巧"
                    },
                    {
                        "url": "www.testingunion.com_demo",
                        "name": "开源优测社区_demo",
                        "desc": "分享各类开源测试技巧_demo"
                    }
                ]
            }
        """

    # 将json串转换成字典
    json_dict = json.loads(json_demo)

    # 遍历字典
    for k, v in json_dict.items():
        # 输出第一层级, k 为 weixin、 web;  v 为 其对应的列表即 [] 中的数据
        print(k, " : ", v)
        for data in v:
            # 遍历列表
            # v 为 []
            for data_k, data_v in data.items():
                # 每个data为[]中的一个字典
                # 遍历列表中的字典
                print("    ", data_k, " : ", data_v)

