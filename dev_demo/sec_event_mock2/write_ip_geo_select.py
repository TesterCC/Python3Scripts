# coding=utf-8
"""
DATE:   2022/1/13
AUTHOR: TesterCC
"""
from collections import namedtuple
from dup_merge_data.sec_event_mock2.sec_event_data import *

area_select_ret = []
def write_ip_area_select():
    IP2GEO = namedtuple("IP2GEO", "ip,area")

    area_list = [i.area for i in map(IP2GEO._make, csv.reader(open("ip_geo_map_2w.csv", "r"))) if i.area != "东京都"]
    # print(len(area_list))
    area_select = list(set(area_list))
    # print(len(area_select))
    # print(area_select)
    for index,area in enumerate(area_select):
        area_select_ret.append({
            "id": index+1,
            "area": area
        })
    # print(area_select_ret)

    write_json("./area.json", area_select_ret)

if __name__ == '__main__':
    write_ip_area_select()