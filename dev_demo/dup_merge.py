# 用Python3将以上数据根据sip和dip进行去重，当sip和dip相同但sport或dport不同时，要合并到sports或的dports字段中。
data = {
    "list": [
        {
            "protocol": "tcp",
            "sip": "172.16.2.99",
            "dip": "172.16.3.99",
            "sport": 41696,
            "dport": 82
        },
        {
            "protocol": "tcp",
            "sip": "172.16.3.99",
            "dip": "172.16.4.99",
            "sport": 41698,
            "dport": 81
        },
        {
            "protocol": "tcp",
            "sip": "172.16.3.100",
            "dip": "172.16.3.99",
            "sport": 41700,
            "dport": 82
        },
        {
            "protocol": "tcp",
            "sip": "172.16.4.100",
            "dip": "172.16.4.99",
            "sport": 41700,
            "dport": 81
        },
        {
            "protocol": "tcp",
            "sip": "172.16.3.100",
            "dip": "172.16.3.99",
            "sport": 41698,
            "dport": 82
        },
        {
            "protocol": "tcp",
            "sip": "172.16.3.100",
            "dip": "172.16.3.99",
            "sport": 41696,
            "dport": 82
        },
        {
            "protocol": "tcp",
            "sip": "172.16.2.99",
            "dip": "172.16.3.99",
            "sport": 41700,
            "dport": 82
        },
        {
            "protocol": "tcp",
            "sip": "172.16.3.99",
            "dip": "172.16.4.99",
            "sport": 41700,
            "dport": 81
        },
        {
            "protocol": "tcp",
            "sip": "172.16.1.99",
            "dip": "172.16.2.99",
            "sport": 41696,
            "dport": 83
        },
        {
            "protocol": "tcp",
            "sip": "172.16.2.100",
            "dip": "172.16.2.99",
            "sport": 41696,
            "dport": 83
        },
        {
            "protocol": "tcp",
            "sip": "172.16.2.99",
            "dip": "172.16.3.99",
            "sport": 41698,
            "dport": 82
        },
        {
            "protocol": "tcp",
            "sip": "172.16.4.100",
            "dip": "172.16.4.99",
            "sport": 41698,
            "dport": 81
        },
        {
            "protocol": "tcp",
            "sip": "172.16.5.100",
            "dip": "172.16.5.99",
            "sport": 41696,
            "dport": 80
        },
        {
            "protocol": "tcp",
            "sip": "172.16.4.99",
            "dip": "172.16.5.99",
            "sport": 41696,
            "dport": 80
        },
        {
            "protocol": "tcp",
            "sip": "172.16.3.99",
            "dip": "172.16.4.99",
            "sport": 41696,
            "dport": 81
        }
    ]
}

filter_packet_list = data["list"]
print("filter_packet_list length: ", len(filter_packet_list))

ret = []

seen = set()

for packet in filter_packet_list:

    if (packet['protocol'], packet['sip'], packet['dip']) not in seen:
        packet['sports'] = [packet['sport']]
        packet['dports'] = [packet['dport']]
        ret.append(packet)

        seen.add((packet['protocol'], packet['sip'], packet['dip']))

    else:
        for item in ret:
            if item['protocol'] == packet['protocol'] and item['sip'] == packet['sip'] and item['dip'] == packet['dip']:
                item['sports'].append(packet['sport'])
                item['dports'].append(packet['dport'])

# 输出清理后的数据
for item in ret:
    item['sports'] = list(set(item['sports']))
    item['dports'] = list(set(item['dports']))

print(len(ret), ret)
# [{'protocol': 'tcp', 'sip': '172.16.2.99', 'dip': '172.16.3.99', 'sport': 41696, 'dport': 82, 'sports': [41696, 41698, 41700], 'dports': [82]}, {'protocol': 'tcp', 'sip': '172.16.3.99', 'dip': '172.16.4.99', 'sport': 41698, 'dport': 81, 'sports': [41696, 41698, 41700], 'dports': [81]}, {'protocol': 'tcp', 'sip': '172.16.3.100', 'dip': '172.16.3.99', 'sport': 41700, 'dport': 82, 'sports': [41696, 41698, 41700], 'dports': [82]}, {'protocol': 'tcp', 'sip': '172.16.4.100', 'dip': '172.16.4.99', 'sport': 41700, 'dport': 81, 'sports': [41698, 41700], 'dports': [81]}, {'protocol': 'tcp', 'sip': '172.16.1.99', 'dip': '172.16.2.99', 'sport': 41696, 'dport': 83, 'sports': [41696], 'dports': [83]}, {'protocol': 'tcp', 'sip': '172.16.2.100', 'dip': '172.16.2.99', 'sport': 41696, 'dport': 83, 'sports': [41696], 'dports': [83]}, {'protocol': 'tcp', 'sip': '172.16.5.100', 'dip': '172.16.5.99', 'sport': 41696, 'dport': 80, 'sports': [41696], 'dports': [80]}, {'protocol': 'tcp', 'sip': '172.16.4.99', 'dip': '172.16.5.99', 'sport': 41696, 'dport': 80, 'sports': [41696], 'dports': [80]}]