import ipaddress
import json
import os
import sys
import string
import random
import time


# version 9

mock_tree = dict()

# root config
root_ip = "192.168.120.12"
root_port = 2222

# 生成ip的起始ip段
generate_start_ip = '192.168.55.1'


# # 10002是要生成节点的数量，需要是3的倍数
node_count = 10000


def generate_ip_list(start_ip, n):
    ip_list = []
    current_ip = ipaddress.IPv4Address(start_ip)

    for _ in range(n):
        ip_list.append(str(current_ip))
        current_ip += 1

    return ip_list


def group_ips(ip_list, group_size):
    return [ip_list[i:i + group_size] for i in range(0, len(ip_list), group_size)]


def get_random_str(length):
    value = ''.join(random.sample(string.ascii_letters + string.digits, length))
    return value


def get_random_str_v1(length):
    value = ''.join(random.sample(string.ascii_lowercase + string.digits, length))
    return value


def gen_random_key_v0():
    # generate random key, 24 bytes
    key1 = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    key2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    gen_key = f"{key1}/{key2}=="
    return gen_key


def gen_random_key_v1():
    # generate random key, 24 bytes
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
    gen_key = f"{key}=="
    return gen_key


def get_random_cipher_suite():
    cs = ["aes", "rc6"]
    # return str
    return random.choice(cs)


def get_random_fake_protocol():
    fake_protocol = ["ssh", "telnets", "netflow", "snmp", "https"]
    # return str
    return random.choice(fake_protocol)


def get_random_port():
    return random.randint(29000, 61000)


def export_mock_tree(tree_data, export_path="."):
    with open(f'{export_path}/mock_tree.json', 'w') as f:
        f.seek(0)
        f.truncate()
        json.dump(tree_data, f, indent=4)


def gen_root_node(real=True):
    node_info = dict()
    node_id = get_random_str_v1(8)
    node_info["id"] = node_id

    node_info["friendly_name"] = "root"
    node_info["control_key"] = gen_random_key_v1()
    node_info["neighbor_key_for_parent"] = gen_random_key_v0()
    node_info["neighbor_key_for_children"] = gen_random_key_v0()
    node_info["cipher_suite"] = get_random_cipher_suite()
    node_info["public_ip"] = root_ip
    node_info["public_port"] = int(root_port)
    node_info["listen_ip"] = "0.0.0.0"
    node_info["listen_port"] = int(root_port)
    node_info["fake_protocol"] = get_random_fake_protocol()
    node_info["outbound_only"] = False

    if real:
        # write root info directly
        node_info = {
            "id": "m7jao8sj",
            "friendly_name": "root",
            "control_key": "bFAjH4CFWmDxDulmQCbVSQ==",
            "neighbor_key_for_parent": "10/h3herYo9oFCymh7wiwA==",
            "neighbor_key_for_children": "wbsOV4O5QH6juQMlJ21YEQ==",
            "cipher_suite": "rc6",
            "public_ip": "192.168.120.12",
            "public_port": 2222,
            "listen_ip": "0.0.0.0",
            "listen_port": 2222,
            "fake_protocol": "https",
            "outbound_only": False
        }

    return node_info


# non root node, round(time.time()*1000):parent_tid
def gen_non_root_node(pid=None, ip=None, port=None, pre="", outbound_only=False):
    node_info = dict()

    if pid and ip and port:
        node_id = get_random_str_v1(8)
        node_info["id"] = node_id

        # node_info["friendly_name"] = f"{round(time.time() * 1000)}:{pre}:{pid}"
        node_info["friendly_name"] = f"{pre}:{pid}"
        node_info["control_key"] = gen_random_key_v1()
        node_info["neighbor_key_for_parent"] = gen_random_key_v0()
        node_info["neighbor_key_for_children"] = gen_random_key_v0()
        node_info["cipher_suite"] = get_random_cipher_suite()
        node_info["public_ip"] = ip
        node_info["public_port"] = int(port)
        node_info["listen_ip"] = "0.0.0.0"
        node_info["listen_port"] = int(port)
        node_info["fake_protocol"] = get_random_fake_protocol()
        node_info["outbound_only"] = outbound_only
    else:
        print("[E] please check must args")
        raise RuntimeError
    return node_info


def get_next_batch(ip_list, batch_size=1000):
    while ip_list:
        batch = ip_list[:batch_size]
        ip_list = ip_list[batch_size:]
        yield batch


def gen_mock_tree(node_count=99):
    mock_tree["known_nodes"] = list()
    mock_tree["me"] = None
    mock_tree["my_children"] = list()
    mock_tree["known_topology"] = list()
    mock_tree["node_heartbeat_time"] = dict()

    # step 1: generate root node
    root_node = gen_root_node(real=True)
    root_node_id = root_node["id"]
    print(f"[D] root_node_id: {root_node_id}")

    # step 2: add root node info in mock tree
    mock_tree["known_nodes"].append(root_node)
    mock_tree["me"] = root_node_id

    # step 3: loop generate 3-level node info and add info in mock tree
    start_ip = generate_start_ip
    ip_count = node_count
    ip_list = generate_ip_list(start_ip, ip_count)
    grouped_ips = group_ips(ip_list, 3)

    print("gen ip list length: ", len(ip_list))
    # insert_device_info_by_ips(ip_list)

    count = 1
    for gips in grouped_ips:
        inner_count = 1
        ipa, ipb, ipc = gips

        # level 1
        ipa_node = gen_non_root_node(pid=root_node_id, ip=ipa, port=get_random_port(), pre=f"{count}-{inner_count}")
        ipa_node_id = ipa_node['id']

        mock_tree["known_nodes"].append(ipa_node)
        mock_tree["my_children"].append(ipa_node_id)  # just ip a

        node_topo = dict()
        node_topo['child'] = ipa_node_id
        node_topo['parent'] = root_node_id
        node_topo['candidate_parents'] = [root_node_id]
        mock_tree["known_topology"].append(node_topo)

        mock_tree["node_heartbeat_time"][ipa_node_id] = round(time.time() * 1000)

        # level 2
        ipb_node = gen_non_root_node(pid=ipa_node_id, ip=ipb, port=get_random_port(), pre=f"{count}-{inner_count + 1}")
        ipb_node_id = ipb_node['id']

        mock_tree["known_nodes"].append(ipb_node)

        node_topo = dict()
        node_topo['child'] = ipb_node_id
        node_topo['parent'] = ipa_node_id
        node_topo['candidate_parents'] = [ipa_node_id]
        mock_tree["known_topology"].append(node_topo)

        mock_tree["node_heartbeat_time"][ipb_node_id] = round(time.time() * 1000)

        # level 3
        ipc_node = gen_non_root_node(pid=ipb_node_id, ip=ipc, port=get_random_port(), pre=f"{count}-{inner_count + 2}",
                                     outbound_only=True)
        ipc_node_id = ipc_node['id']

        mock_tree["known_nodes"].append(ipc_node)

        node_topo = dict()
        node_topo['child'] = ipc_node_id
        node_topo['parent'] = ipb_node_id
        node_topo['candidate_parents'] = [ipb_node_id]
        mock_tree["known_topology"].append(node_topo)

        mock_tree["node_heartbeat_time"][ipc_node_id] = round(time.time() * 1000)

        count += 1

    # step 4: export mock_tree.json
    export_mock_tree(mock_tree)
    print(f"total: {(count - 1) * 3}")
    print(f"[D] Finish generate at: {os.getcwd()}/mock_tree.json...")


def gen_mock_tree_v9(node_count=0):
    # print(f"[D] node_count: {node_count}, group_count: {group_count}")
    # if node_count == 0 or group_count == 0:
    #     raise "[D] count is zero..."

    mock_tree["known_nodes"] = list()
    mock_tree["me"] = None
    mock_tree["my_children"] = list()
    mock_tree["known_topology"] = list()
    mock_tree["node_heartbeat_time"] = dict()

    # step 1: generate root node
    root_node = gen_root_node(real=True)
    root_node_id = root_node["id"]
    print(f"[D] root_node_id: {root_node_id}")

    # step 2: add root node info in mock tree
    mock_tree["known_nodes"].append(root_node)
    mock_tree["me"] = root_node_id

    # step 3: loop generate 3-level node info and add info in mock tree
    start_ip = generate_start_ip
    ip_count = node_count
    ip_list = generate_ip_list(start_ip, ip_count)
    print("[D] ip_list length: ", len(ip_list))
    # print("[D] ip_list 10 : ", ip_list[:10])

    count = 0
    while ip_list:
        gips = ip_list[:1000]
        ip_list = ip_list[1000:]

        ipas, ipbs, ipcs = gips[0:1], gips[1:11], gips[11:1000]
        print(f"[D] ipas length: {len(ipas)}")
        print(f"[D] ipbs length: {len(ipbs)}")
        print(f"[D] ipcs length: {len(ipcs)}")
        count += 1
        print(count, "--" * 33)

        ipa = ipas[0]
        # level 1
        ipa_node = gen_non_root_node(pid=root_node_id, ip=ipa, port=get_random_port(), pre=f"1-{count}")
        ipa_node_id = ipa_node['id']

        mock_tree["known_nodes"].append(ipa_node)
        mock_tree["my_children"].append(ipa_node_id)  # just ip a

        node_topo = dict()
        node_topo['child'] = ipa_node_id
        node_topo['parent'] = root_node_id
        node_topo['candidate_parents'] = [root_node_id]
        mock_tree["known_topology"].append(node_topo)

        mock_tree["node_heartbeat_time"][ipa_node_id] = round(time.time() * 1000)

        inner_count = 0
        for ipb in ipbs:
            # level 2
            inner_count += 1
            ipb_node = gen_non_root_node(pid=ipa_node_id, ip=ipb, port=get_random_port(),
                                         pre=f"2-{count}-{inner_count}")
            ipb_node_id = ipb_node['id']

            mock_tree["known_nodes"].append(ipb_node)

            node_topo = dict()
            node_topo['child'] = ipb_node_id
            node_topo['parent'] = ipa_node_id
            node_topo['candidate_parents'] = [ipa_node_id]
            mock_tree["known_topology"].append(node_topo)

            mock_tree["node_heartbeat_time"][ipb_node_id] = round(time.time() * 1000)

            print(f"[D] ipcs: {len(ipcs)}")
            print("-" * 33)

            _ipcs = ipcs[:100]
            ipcs = ipcs[100:]
            print(f"[D] length： {len(_ipcs)}, xxx: {_ipcs}")

            bottom_count = 0
            while _ipcs:
                for ipc in _ipcs:
                    # level 3
                    bottom_count += 1
                    ipc_node = gen_non_root_node(pid=ipb_node_id, ip=ipc, port=get_random_port(),
                                                 pre=f"{count}-{inner_count}-{bottom_count}",
                                                 outbound_only=True)
                    ipc_node_id = ipc_node['id']

                    mock_tree["known_nodes"].append(ipc_node)

                    node_topo = dict()
                    node_topo['child'] = ipc_node_id
                    node_topo['parent'] = ipb_node_id
                    node_topo['candidate_parents'] = [ipb_node_id]
                    mock_tree["known_topology"].append(node_topo)

                    mock_tree["node_heartbeat_time"][ipc_node_id] = round(time.time() * 1000)
                    _ipcs.remove(ipc)
                    # print(f"[D] {ipa} -- {ipb} -- {ipc}")

    # step 4: export mock_tree.json
    export_mock_tree(mock_tree)
    # print(f"total: {(count - 1) * 3}")
    print(f"[D] count: {count}")
    print(f"[D] Finish generate at: {os.getcwd()}/mock_tree.json...")


def read_tree_info(path=""):
    with open(path) as f:
        tree_json = json.load(f)

    known_nodes = tree_json.get('known_nodes')
    print(len(known_nodes))
    # known_topology = tree_json.get('known_topology')


if __name__ == '__main__':
    node_count = 10000
    # group_count = 1000
    # gen_mock_tree_v6(node_count=node_count, group_count=group_count)
    # gen_mock_tree_v7(node_count=node_count)
    gen_mock_tree_v9(node_count=node_count)  # 完成计划，注意索引

    read_tree_info("./mock_tree.json")
