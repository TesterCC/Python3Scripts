# coding=utf-8
"""
DATE:   2022/1/12
AUTHOR: TesterCC
"""

'''
统计 analysis_data.json 中 12000 条数据的信息
需求：
在event sec中统计：源IP TOP5、目的IP TOP5、源地区分布、目的地区分布、攻击类型TOP5
统计结果写入 analysis_data_statistics.json 文件中

不方便就是自己先构造几个测试数据
'''

# get_top5_src_area    源IP TOP5
# get_top5_dst_area    目的IP TOP5
# get_src_distribution 源地区分布
# get_dst_distribution 目的地区分布
# get_top5_attack_type 攻击类型TOP5

from dev_demo.sec_event_mock2.sec_event_data import read_json, write_json

data = read_json("./analysis_data.json")  # list, 12000

stat_src = dict()
def get_top5_src_area():
    # 源IP TOP5
    for i in data:
        if i.get('src_area') not in stat_src.keys():
            stat_src[i.get('src_area')] = 1
        else:
            stat_src[i.get('src_area')] += 1

    order_stat_src = sorted(stat_src.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    ret = []
    for i in order_stat_src[:5]:
        at, count = i
        ret.append({
            "src": at,
            "count": count
        })

    # print(ret)
    return ret


stat_dst = dict()
def get_top5_dst_area():
    # 目的IP TOP5
    for i in data:
        if i.get('dst_area') not in stat_dst.keys():
            stat_dst[i.get('dst_area')] = 1
        else:
            stat_dst[i.get('dst_area')] += 1

    order_stat_dst = sorted(stat_dst.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    ret = []
    for i in order_stat_dst[:5]:
        at, count = i
        ret.append({
            "dst": at,
            "count": count
        })

    # print(ret)
    return ret

stat_src_area = dict()
def get_src_distribution():
    # 源地区分布 是全部
    for i in data:
        if i.get('src_area') == "东京都":   # 因为原数据中有外国，特别处理下。
            continue
        elif i.get('src_area') not in stat_src_area.keys():
            stat_src_area[i.get('src_area')] = 1
        else:
            stat_src_area[i.get('src_area')] += 1

    order_stat_src_area = sorted(stat_src_area.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    ret = []
    for i in order_stat_src_area:
        at, count = i
        ret.append({
            "src_area": at,
            "count": count
        })

    sum_src = sum(i.get('count') for i in ret)  # 数据总数用于计算地区数据占比
    # print(f"sum src : {sum_src}")
    ret2 = []
    for i in ret:
        ret2.append({
            "src_area": i.get('src_area'),
            "count": i.get('count'),
            "percent": '{:.2%}'.format(i.get('count') / sum_src)
        })
    # print(ret2)

    ret_data = dict()    # get_src_distribution 全部需要返回的数据
    ret_data['area_count'] = len(ret)   # 源地区数据
    ret_data['area_data'] = ret2

    # print(ret_data)
    return ret_data


stat_dst_area = dict()
def get_dst_distribution():
    # 目的地区分布
    for i in data:
        if i.get('dst_area') == "东京都":   # 因为原数据中有外国，特别处理下。
            continue
        elif i.get('dst_area') not in stat_dst_area.keys():
            stat_dst_area[i.get('dst_area')] = 1
        else:
            stat_dst_area[i.get('dst_area')] += 1

    order_stat_dst_area = sorted(stat_dst_area.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    ret = []
    for i in order_stat_dst_area:
        at, count = i
        ret.append({
            "dst_area": at,
            "count": count
        })

    sum_dst = sum(i.get('count') for i in ret)  # 数据总数用于计算地区数据占比
    # print(f"sum dst : {sum_dst}")
    ret2 = []
    for i in ret:
        ret2.append({
            "dst_area": i.get('dst_area'),
            "count": i.get('count'),
            "percent": '{:.2%}'.format(i.get('count') / sum_dst)
        })
    # print(ret2)

    ret_data = dict()    # get_dst_distribution 全部需要返回的数据
    ret_data['area_count'] = len(ret)   # 源地区数据
    ret_data['area_data'] = ret2

    # print(ret_data)
    return ret_data


stat_at = dict()
def get_top5_attack_type():
    # 攻击类型TOP5
    for i in data:
        if i.get('type') not in stat_at.keys():
            stat_at[i.get('type')] = 1
        else:
            stat_at[i.get('type')] += 1

    # print(stat_at)
    order_stat_at = sorted(stat_at.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    # print(order_stat_at[:5])
    ret = []
    for i in order_stat_at[:5]:
        at, count = i
        ret.append({
            "attack_type": at,
            "count": count
        })

    # print(ret)
    return ret


def launch():
    ret = dict()
    # 调用各个函数统一生成统计结果
    ret['top5_attack_type'] = get_top5_attack_type()
    ret['top5_src_area'] = get_top5_src_area()
    ret['top5_dst_area'] = get_top5_dst_area()
    ret['src_distribution'] = get_src_distribution()
    ret['dst_distribution'] = get_dst_distribution()

    print(ret)

    # write_json
    write_json('./analysis_data_statistics.json', ret)


if __name__ == '__main__':
    # get_dst_distribution()
    # get_src_distribution()
    # get_top5_dst_area()
    # get_top5_src_area()
    # get_top5_attack_type()
    launch()
