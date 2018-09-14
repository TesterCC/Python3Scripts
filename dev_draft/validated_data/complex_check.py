#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/14 15:23'

from cerberus import Validator


def check_kwargs(kwargs):
    """
    检测必要的字段是否满足创建要求
    """

    schema = {
        "name": {"type": "string", "required": True},
        "nick_name": {"type": "string"},
        "class_info": {   # 注意这里也是要标注rule的
            "type": "dict", "schema": {
                "class_type": {"type": "integer", "required": True},
                "class_fee": {"type": "integer"}
            }
        },
    }

    v = Validator()
    v.allow_unknown = True  # default False
    flag = v(kwargs, schema),

    ret = {
        "flag": flag,
        "mag": "订单信息填写不符合要求" if not flag else "success",
        "data": v.errors,
    }
    return ret


if __name__ == '__main__':
    data_01 = {"name": "tester1",
               "class_info": {
                   "class_type": 0
               }
               }

    data_02 = {"name": "tester2",
               "nick_name": "cute_cat",
               "class_info": {
                   "class_type": 1,
                   "class_fee": 300
               }
               }

    data_03 = {"name": "tester3",
               "class_info": {
                   "class_type": 0
               },
               "vip": True  # can add unknown
               }

    # error test_case
    data_04 = {"name": "tester4",
               "class_info": {
                   "class_type": ''
               },
               }  # error

    print(data_04)
    print(check_kwargs(data_04))
