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
req = req.decode("utf-8")  # str
# print(type(req))

# 将已编码的json字符串解码为Python对象
req_dict = json.loads(req)
print("req_dict type is %s" % type(req_dict))


def get_id():
    return str(req_dict['event']['id'])


def get_event_name():
    return req_dict['event']['event_name']


def get_event_id():
    return req_dict['event']['event_id']     # 1322992792


def get_event_status():
    return req_dict['event']['event_status']


def get_event_url():
    event_url = DOMAIN_URL + req_dict['event']['event_url']
    return event_url


def get_event_begin_time():
    return req_dict['event']['event_begin_time']


def get_event_end_time():
    return req_dict['event']['event_end_time']


def get_event_img_v2():
    d_event = req_dict.get('event')
    # print("Output event_img list:")
    # print(d_event.get('event_img'))
    for item in d_event.get('event_img'):
        # print(item)
        # print(type(item))   # dict
        return item['server__name'] + item['urls']


def get_event_tag_info_v2():
    """
    v2 return tag 1 by 1
    TODO some bug need to fix
    :return:
    """
    # dict can use get() and items()
    d_event = req_dict.get('event')
    # print(d_event)
    # print(type(d_event))
    # print('++++'*40)
    # for k,v in d_event.items():
    #     print("{0}-->{1}".format(k, v))
    # print('++++'*40)

    # print(d_event.get('event_tag_info'))
    for i in d_event.get('event_tag_info'):
        print(i['name'])


def get_event_cat_info():
    d_event = req_dict.get('event')

    for i in d_event.get('event_cat_info'):
        return i['name']


def get_event_tag_info():
    """
    v1
    :return: a tag list
    """
    event_tag_list = req_dict['event']['event_tag_info']
    res_list = [item[key] for item in event_tag_list for key in item if isinstance(item[key], str)]

    return res_list


# get article content
def get_event_content():
    """
    获取会议内容html important
    :return:
    """
    d_event = req_dict.get('event')

    for items in d_event.get('properties'):
        for k, v in items.items():
            if k == 'children':
                # print(type(v))   # list
                for i in v:
                    # print(type(i))  # dict
                    # print(type(i.get('value')))   # str
                    return i.get('value')


def get_event_content_v2():
    """
    FIXME issue , get all html event content
    :return:
    """
    event_info = req_dict.get('event', '').get('properties', '')
    event_content = "".join([i.get('value', "") for items in event_info for k, v in items.items() if k == 'children' for i in v])
    return event_content


def get_event_schedule():
    """
    获取会议日程html
    TODO 学习一下这种写发重构get_event_content()
    important, all event content in this node
    :return:
    """
    event_info = req_dict.get('event')
    event_schedules = [propertie.get("value", "") for propertie in event_info.get("properties") if
                      u"日程" in propertie.get("name", "")]     # property是保留关键字

    event_schedule = event_schedules[0] if event_schedules else ""
    return event_schedule


def get_event_schedule_v2():
    """
    这种写发，前面加个join 就不用判断是否为空了
    :return:
    """
    event_info = req_dict.get('event')
    properties = event_info.get("properties")
    event_schedule = "<br/>".join([propertie.get("value", "") for propertie in properties if u"日程" in
                                   propertie.get("name", "")])
    return event_schedule


def get_article_message():
    """
    拼接需求中的文章的模版
    :return:
    """
    prefix = ""
    content_message = "<b>会议内容</b>" + get_event_content() + "<b>会议日程</b>" + get_event_schedule()
    suffix = ""

    return content_message


# Tools Method
def list_all_dict(dict_a=req_dict):
    """
    嵌套字典环境下获取所有内容
    :param dict_a:
    :return:
    """

    if isinstance(dict_a, dict):  # 使用isinstance检测数据类型

        for x in range(len(dict_a)):

            temp_key = list(dict_a.keys())[x]
            # 原文 temp_key = dict_a.keys()[x] 报错'dict_keys' object does not support indexing
            # 由于python3改变了dict.keys,返回的是dict_keys对象,支持iterable 但不支持indexable，我们可以将其明确的转化成list

            temp_value = dict_a[temp_key]

            print("%s : %s" % (temp_key, temp_value))

            list_all_dict(temp_value)  # 递归, 自我调用实现无限遍历


def dict_get(dict_input=req_dict, objkey='', default=None):
    """
    获取字典中的objkey对应的值，适用于字典嵌套 -- 不太好用
    :param dict: 字典
    :param objkey: 目标key
    :param default: 找不到时返回的默认值
    :return:
    """
    tmp = dict_input
    for k, v in tmp.items():
        if k == objkey:
            return v
        else:
            if isinstance(v, dict):
                ret = dict_get(v, objkey, default)
                if ret is not default:
                    return ret
    return default


# TODO write code  draft >>>>>>>>>>>>>>>>>
def get_event_properties():
    """
    important, all event content in this node
    :return:
    """
    d_event = req_dict.get('event')

    for items in d_event.get('properties'):
        # print(type(items))
        # print(items)
        for k, v in items.items():
            print("{}---------->{}".format(k, v))


def get_event_intro():
    pass


if __name__ == '__main__':
    # print(get_event_url())
    # print(get_id())
    # print(get_event_id())
    print("＊＊＊＊" * 30)
    # print(get_event_end_time())
    # print(get_event_name())
    # print(get_event_tag_info())
    # print(get_event_content())

    # print(get_event_properties())
    # print(get_event_tag_info_v2())
    # print(get_event_img_v2())

    # print(get_event_cat_info())

    # Parser Json Data
    # print(get_event_properties())
    # print(get_event_content())
    # print(get_event_schedule())
    # print(get_event_schedule_v2())
    # print(get_event_content())
    # print(get_event_content_v2())  # bug

    # list_all_dict()

    # print(dict_get(objkey='properties', default=None))

    # print(get_article_message())

    content_message = get_article_message()    # str
    print(content_message)




