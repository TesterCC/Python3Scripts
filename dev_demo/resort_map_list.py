data = [
    {"id": 1, "name": "Cisco"},
    {"id": 2, "name": "Juniper"},
    {"id": 3, "name": "Huawei"},
    {"id": 4, "name": "FortiGate"},
    {"id": 5, "name": "MikroTik"},
    {"id": 6, "name": "DrayTek"},
    {"id": 7, "name": "NETGEAR"},
    {"id": 8, "name": "TP-Link"},
    {"id": 9, "name": "D-Link"},
    {"id": 10, "name": "CheckPoint"},
    {"id": 11, "name": "Sophos"}
]

# 需求，按name字段英文名称排序
sorted_data = sorted(data, key=lambda x: x['name'])
print("-" * 33)
print(sorted_data)
