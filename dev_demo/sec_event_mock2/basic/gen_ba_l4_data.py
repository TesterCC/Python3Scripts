# coding=utf-8
"""
DATE:   2022/1/11
AUTHOR: TesterCC
"""

'''
根据csv生成L4，生成sec_event 攻击类型 静态 json 数据
'''

from collections import namedtuple

import csv

from dup_merge_data.sec_event_mock2.sec_event_data import write_json

def write_attack_type_select():
    """
    写攻击类型下拉框数据
    """
    NAO_L4 = namedtuple("NAO_L4", "ba_id, ba_name,ba_zh_name,weight")

    nao_l4_list = []
    # map1 = map(NAO_L4._make, csv.reader(open("NL4.csv","r")))
    # print("map: ", list(map1))
    for l4 in map(NAO_L4._make, csv.reader(open("NL4.csv","r"))):
        # print(l4.ba_id, l4.ba_zh_name)
        nao_l4_list.append({
            "ba_id": l4.ba_id,
            "ba_name": l4.ba_name,
            "ba_zh_name": l4.ba_zh_name,
            "weight": int(l4.weight)
        })

    nao_l4_order_list = sorted(nao_l4_list, key=lambda e: e['weight'], reverse=True)
    print(f"total nao_l4_list: {len(nao_l4_order_list)}")
    print(nao_l4_order_list)

    write_json("./attack_type.json", nao_l4_order_list)


def read_ba_csv():
    NAO_L4 = namedtuple("NAO_L4", "ba_id, ba_name,ba_zh_name,weight")

    nao_l4_list = []
    # map1 = map(NAO_L4._make, csv.reader(open("NL4.csv","r")))
    # print("map: ", list(map1))
    for l4 in map(NAO_L4._make, csv.reader(open("NL4.csv","r"))):
        # print(l4.ba_id, l4.ba_zh_name)
        nao_l4_list.append({
            "ba_id": l4.ba_id,
            "ba_name": l4.ba_name,
            "ba_zh_name": l4.ba_zh_name,
            "weight": int(l4.weight)
        })

    nao_l4_order_list = sorted(nao_l4_list, key=lambda e: e['weight'], reverse=True)

    print(f"total nao_l4_list: {len(nao_l4_order_list)}")

    return nao_l4_list

if __name__ == '__main__':
    # # read_ba_csv()
    # nao_l4_list = read_ba_csv()
    # nao_l4_order_list = sorted(nao_l4_list, key=lambda e: e['weight'], reverse=True)
    # attack_type = [i.get('ba_zh_name') for i in nao_l4_list]
    # print(attack_type)
    #
    # print("----------"*10)
    #
    #
    # # 可以做权重排序，但是加权算法得专门写，故目前还是直接随机，没有按加权做随机
    # sorted_attack_type = [i.get('ba_zh_name') for i in nao_l4_order_list]
    # print(sorted_attack_type)

    write_attack_type_select()
