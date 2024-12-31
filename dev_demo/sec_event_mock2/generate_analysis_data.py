# coding=utf-8
"""
DATE:   2021/5/18
AUTHOR: Yanxi Li
"""
from collections import namedtuple
from dup_merge_data.sec_event_mock2.sec_event_data import *


# 按照新蓝湖设计图构造数据，最后要写入json文件，方便后面做统计
# right data


def get_random_ip_geo():
    IP2GEO = namedtuple("IP2GEO", "ip,area")
    ip2geo_list = []

    for i in map(IP2GEO._make, csv.reader(open("ip_geo_map_2w.csv", "r"))):
        # print(i.area, i.ip)
        ip2geo_list.append({
            "ip": i.ip,
            "area": i.area
        })

    # print(random.choice(ip2geo_list))
    return random.choice(ip2geo_list)


def write_json_v2(config_path, json_obj):
    with open(config_path, 'w', encoding="utf-8") as f:
        f.seek(0)
        f.truncate()
        json.dump(json_obj, f, indent=4, ensure_ascii=False)
    print("Write json file in: ", config_path)


def gen_analysis_json(count=1000):
    ret = []
    for i in range(count):
        data = dict()
        data['time'] = get_random_time()
        data['title'] = get_random_web_title()
        data['type'] = get_random_attack_type()
        data['name'] = get_random_name()  # 人名

        src_info = get_random_ip_geo()
        data['src'] = src_info.get('ip')
        data['src_area'] = src_info.get('area')

        dst_info = get_random_ip_geo()
        data['dst'] = dst_info.get('ip')
        data['dst_area'] = dst_info.get('area')

        # print(f'src info: {src_info}')
        # print(f'dst info: {dst_info}')
        # print(data)

        ret.append(data)

    print(f"ret length: {len(ret)}")
    # write_json_v2("./analysis_data_v2_{}.json".format(int(time.time())), ret)
    write_json("./analysis_data_v2_{}.json".format(int(time.time())), ret)

'''
ret length: 1000
Write json file in:  ./analysis_data_v2_1641972271.json
cost time: 47.027244091033936

ret length: 12000
Write json file in:  ./analysis_data_v2_1641972982.json
cost time: 595.9579706192017
'''

if __name__ == '__main__':
    st = time.time()
    gen_analysis_json(count=12000)
    print(f"cost time: {time.time() - st} seconds.")
    # get_random_ip_geo()
