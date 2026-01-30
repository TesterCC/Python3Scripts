# insert tree_1009.json ip into device_info

import ipaddress
import json
import os
import sys
import random
import time

sys.path.append('/opt/i_cm')
config_center_dir = r"/opt/i_cm/"

import i_cm

config_file = '/opt/i_cm/controlled/tree.json'


# def write_node_heartbeat_time():
#     with open(config_file) as f:
#         tree_json = json.load(f)
#         known_nodes = tree_json.get('known_nodes')
#
#         tree_json["node_heartbeat_time"] = dict()
#         for node in known_nodes:
#             tree_json["node_heartbeat_time"][node.get('id')] = round(time.time() * 1000)
#
#         with open(f'./mock_tree.json', 'w') as f:
#             f.seek(0)
#             f.truncate()
#             json.dump(tree_json, f, indent=4)


def get_all_nodes_ips():
    with open(config_file) as f:
        tree_json = json.load(f)

    # root_tid = tree_json.get('me')
    known_nodes = tree_json.get('known_nodes')
    # known_topology = tree_json.get('known_topology')

    node_ips = [node.get("public_ip") for node in known_nodes]
    return node_ips


def insert_device_info_by_ips(ip_list):
    device_id_count = 0
    device_id_count_time = round(time.time() * 1000)

    device_col = i_cm.init_col('device_info')
    device_col.drop()

    device_list = list()
    for ip in ip_list:
        device_id_count += 1
        device = {
            "_id": "%s_%s" % (device_id_count_time, device_id_count),
            "device_ip": ip.split(","),
            "resp_time": round(time.time() * 1000),
            "device_status": "online",
            "device_type": random.choice([1, 2, 3]),
            "device_vendor": "",
            "device_model": "",
            "multi_control": True,
            "os": "",
            "area": "",
            "vrip": True
        }
        device_list.append(device)

    print(len(device_list))
    # print(device_list)

    # insert many to db

    device_col.insert_many(device_list)
    print("[=] Finish insert mock device info in db...")


if __name__ == '__main__':
    # write_node_heartbeat_time()
    node_ips = get_all_nodes_ips()
    print(f'length: {len(node_ips)}')
    # print(f'node_ips: {node_ips}')
    insert_device_info_by_ips(node_ips)
    print("[D] Finish insert device info according tree.json")

