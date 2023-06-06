# coding=utf-8
"""
DATE:   2021/5/18
AUTHOR: Yanxi Li
"""

from dup_merge_data.sec_event_mock.sec_event_data import *

# right data

def gen_analysis_json(count=1000):
    ret = []
    for i in range(count):
        data = {
            "time": get_random_time(),
            "src": get_random_wan_ip(),
            "dst": get_random_wan_ip(),
            "title": get_random_title(),
            "type": get_random_attack_type()
        }

        ret.append(data)

    write_json("./analysis_data_{}.json".format(int(time.time())), ret)


if __name__ == '__main__':
    gen_analysis_json(count=3000)
