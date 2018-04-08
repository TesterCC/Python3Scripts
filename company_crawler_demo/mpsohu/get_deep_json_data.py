#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/8 15:25'


import json
import requests


TARGET_URL = "https://www.huodongjia.com/event-1322992792.html?json=1"
DOMAIN_URL = "https://www.huodongjia.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Host': 'www.huodongjia.com'
}

req = requests.get(TARGET_URL, headers=headers, timeout=10).content
# print(type(req))   # python2 str, python3 bytes

# the JSON object must be str, not 'bytes'
req = req.decode("utf-8")
print(type(req))

# 将已编码的json字符串解码为Python对象
req_dict = json.loads(req)
print("req_dict type is %s" % type(req_dict))

# dict can use get() and items()
d_event = req_dict.get('event')
print(d_event)
print(type(d_event))
print('****'*40)
# print(d_event.items()) # dict_items
for k,v in d_event.items():
    print("{0}-->{1}".format(k, v))
print('****'*40)


print(d_event.get('event_tag_info'))


def get_event_img():
    """
    event_img_list = [{'Asin': b2b}]
    取出其中的value，使用如下代码就可以了
    [item[key] for item in event_img_list for key in item]
    :return:
    """
    event_img_list = req_dict['event']['event_img']
    res_list = [item[key] for item in event_img_list for key in item]
    pic_url = res_list[1]+res_list[2]
    # print(type(pic_url))   # str
    return pic_url


def get_event_tag_info():
    event_tag_list = req_dict['event']['event_tag_info']
    # print(type(event_tag_list))  # list
    # print(event_tag_list)
    # a = []
    # for item in event_tag_list:
    #     for key in item:
    #         if isinstance(item[key], str):
    #             a.append(item[key])
    # return a
    res_list = [item[key] for item in event_tag_list for key in item if isinstance(item[key], str)]

    return res_list




# write for tes draft

def get_event_content():
    event_content_list = req_dict['event']['properties']
    # content_list = [item[key] for item in event_tag_list for key in item]
    a = []
    for item in event_content_list:
        for key in item:
            if isinstance(item[key], str):
                print(item[key])
            elif isinstance(item[key], dict):
                for _key in item[key]:
                    print(_key)


def get_event_intro():
    pass


# def get_event_schedule():
#     event_content_list = req_dict['event']['properties']
#     for item in event_content_list:
#         for key in item:
#             if isinstance(item[key], str):
#                 print(item[key])
#             elif isinstance(item[key], dict):
#                 print(item[key])
#             elif isinstance(item[key], list):
#                 print(item[key])
#             else:
#                 print(item[key])


# def get_event_properties():
#     res = req_dict['event']['properties']
#     print(type(res))  # list

def run(t=req_dict):
    for k, v in t.items():   # Python 3 renamed dict.iteritems -> dict.items
        if isinstance(v, list):
            for element in v:
                run(element)
        elif isinstance(v, dict):
            run(v)
        else:
            print(k, v)
# AttributeError: 'str' object has no attribute 'items'


def print_keyvalue_all(input_json=req):
    key_value=''
    if isinstance(input_json,dict):
        for key in input_json.keys():
            key_value = input_json.get(key)
            if isinstance(key_value,dict):
                print_keyvalue_all(key_value)
            elif isinstance(key_value,list):
                for json_array in key_value:
                    print_keyvalue_all(json_array)
            else:
                print(str(key)+" = "+str(key_value))
    elif isinstance(input_json,list):
        for input_json_array in input_json:
            print_keyvalue_all(input_json_array)


if __name__ == '__main__':
    # print(get_event_img())
    # print(get_event_tag_info())
    # print(get_event_content())

    # print(get_event_properties())
    # get_event_intro()
    print('Start to Test!')
    # print_keyvalue_all()

