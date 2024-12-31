# coding=utf-8
"""
DATE:   2021/1/26
AUTHOR: Yanxi Li
"""

ov = [{'id': 'hebe', 'name': '引擎 基础版'},
      {'id': 'hese', 'name': '引擎 标准版'},
      {'id': 'heee', 'name': '引擎 企业版'},
      {'id': 'heae', 'name': '引擎 高性能版'},
      {'id': 'gbbe', 'name': '知识大脑 基础版'},
      {'id': 'gbse', 'name': '知识大脑 标准版'},
      {'id': 'gbee', 'name': '知识大脑 企业版'},
      {'id': 'gbae', 'name': '知识大脑 高性能版'},
      {'id': 'sabe', 'name': '态势感知 基础版'},
      {'id': 'sase', 'name': '态势感知 标准版'},
      {'id': 'saee', 'name': '态势感知 企业版'},
      {'id': 'saae', 'name': '态势感知 高性能版'}]

pm = {'KBDTD-M': {}}

pm['KBDTD-M']['type_id'] = 'KBDTD-M'
pm['KBDTD-M']['type_name'] = '迁移'

# print("init_dict: \n", pm)

pm['KBDTD-M']['version'] = {}

for item in ov:
    # print(item['id'].upper(), item['name'])
    pm['KBDTD-M']['version']['KBDTD-M-{}'.format(item['id'].upper())] = {
        'id': 'KBDTD-M-{}'.format(item['id'].upper()),
        'name': item['name'],
        'duration': 0,
        'platform': 0,
        'update': 0
    }

print("handle dict: \n", pm)
