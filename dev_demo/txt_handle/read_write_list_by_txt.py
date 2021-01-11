# coding=utf-8
"""
DATE:   2021/1/8
AUTHOR: Yanxi Li
"""

# 1. read audit_ids.txt and device_ids.txt

# 一个或多个数据都可以这样操作
with open('audit_ids.txt', 'r') as f:
    audit_ids = f.readline()  # realine() return str , readlines() return list

audit_ids_list = audit_ids.split(",")

print(type(audit_ids_list))
print(audit_ids_list)

# with open('device_ids.txt', 'r') as f:
#     device_ids = f.readline()  # realine() return str , readlines() return list
#
# device_ids_list = device_ids.split(",")
#
# print(type(device_ids_list))
# print(device_ids_list)


# 2. compare _id
crm_plm_audit_ids_list = ['query:1606631545:0', 'query:1606634566:0', 'query:1606634636:0']

ret = set(audit_ids_list) - set(crm_plm_audit_ids_list)

diff_remote_audit_id = list(ret)
print(diff_remote_audit_id)

# 3. 把list写入 diff_remote_audit_id.txt 中
with open('diff_remote_audit_id.txt', 'w') as f:
    f.write(",".join(diff_remote_audit_id))

print("[+] Diff _ids write in XXX.txt.")