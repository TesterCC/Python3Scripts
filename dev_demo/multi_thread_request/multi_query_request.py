# coding=utf-8
"""
DATE:   2020/11/3
AUTHOR: Yanxi Li
"""
import json

import traceback

import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CONFIG_PATH = "./json_map.json"
LOGIN_URL = "https://127.0.0.1/api/login/"  # sys_login_path if need login

from threading import Thread


def read_json(filename):
    '''
    read all .json file management configuration
    :param filename:
    :return:
    '''
    # 如果文件名不存在，出于安全考虑，直接返回 {}
    json_obj = {}

    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            json_map = json.load(f)

        json_file = json_map.get(filename, None)
        if json_file:
            with open(json_file, 'r', encoding='utf-8') as f:
                json_obj = json.load(f)

    except FileNotFoundError:
        traceback.print_exc()
    return json_obj


def get_cookie():
    """
    定义cookie获取逻辑
    """

    user_info_config = read_json("user_info")

    headers = {"Accept": "application/json, text/plain, */*"}
    payloads = {
        "username": user_info_config['username'],
        "password": user_info_config['password']
    }

    session = requests.Session()

    # 注意参数选择上的坑
    response = session.post(LOGIN_URL, headers=headers, json=payloads, verify=False)

    # print(session.cookies)
    # print(response.json())
    return session


def request(target_url=""):
    if not target_url:
        raise ValueError
    req = get_cookie()
    resp = req.get(target_url)
    print(resp.json())


def multi_threading_query(count=50, target_url=""):
    if not target_url:
        raise ValueError

    # 创建获取url的线程
    url_thread = Thread(target=request(target_url))
    # 详情线程组
    detail_thread = []
    for i in range(count):
        thread2 = Thread(target=request(target_url))
        detail_thread.append(thread2)

    print("detail_thread: ", len(detail_thread))

    # 开启url线程
    url_thread.start()

    for i in range(count):
        # 开启详情进程
        detail_thread[i].start()

    # 等待所有子进程结束
    url_thread.join()
    for i in range(count):
        detail_thread[i].join()


if __name__ == '__main__':
    # req = get_cookie()
    # resp = req.get("https://127.0.0.1/api/type_map/")
    # print(resp.json())

    # multi thread query
    url_path = "/api/type_map/"
    t_url = "https://127.0.0.1{}".format(url_path)
    multi_threading_query(count=20, target_url=t_url)
