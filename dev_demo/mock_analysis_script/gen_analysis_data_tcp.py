# -*- coding: utf8 -*-
import json
import random
import time


def get_random_port():
    port = random.choice(range(11002, 65535))
    return port


"""
1.json: 192.168.121.99 -> 172.16.1.99 -> 172.16.2.99
2.json: 172.16.2.99 -> 172.16.3.99
3.json: 172.16.3.99 -> 192.168.120.99
"""


def get_t_1_1():
    dict_template_1_1 = {
        "sip": "192.168.121.99",
        "sport": get_random_port(),
        "dip": "172.16.1.99",
        "dport": 83,
        "protocol": "tcp"
    }
    return dict_template_1_1


def get_t_1_2():
    dict_template_1_2 = {
        "sip": "172.16.1.99",
        "sport": get_random_port(),
        "dip": "172.16.2.99",
        "dport": 82,
        "protocol": "tcp"
    }
    return dict_template_1_2


def get_t_2_1():
    dict_template_2_1 = {
        "sip": "172.16.2.99",
        "sport": get_random_port(),
        "dip": "172.16.3.99",
        "dport": 81,
        "protocol": "tcp"
    }
    return dict_template_2_1


def get_t_3_1():
    dict_template_3_x = {
        "sip": "172.16.3.99",
        "sport": get_random_port(),
        "dip": "192.168.120.99",
        "dport": 80,
        "protocol": "tcp"
    }
    return dict_template_3_x


def generate_data_1(count=33):
    data = []

    for i in range(count):
        data.append(get_t_1_1())

    for i in range(count):
        data.append(get_t_1_2())

    return data


def generate_data_2(count=33):
    data = []

    for i in range(count):
        data.append(get_t_2_1())

    return data


def generate_data_3(count=33):
    data = []

    for i in range(count):
        data.append(get_t_3_1())

    return data


def generate_all_mock_data():
    gen_data = generate_data_1()
    print("[D] gen_data: ", gen_data)
    with open(f"{round(time.time() * 1000)}.json", "w") as f:
        json.dump(gen_data, f, indent=4)

    gen_data = generate_data_2()
    print("[D] gen_data: ", gen_data)
    with open(f"{round(time.time() * 1000)}.json", "w") as f:
        json.dump(gen_data, f, indent=4)

    gen_data = generate_data_3()
    print("[D] gen_data: ", gen_data)
    with open(f"{round(time.time() * 1000)}.json", "w") as f:
        json.dump(gen_data, f, indent=4)


if __name__ == '__main__':
    generate_all_mock_data()


