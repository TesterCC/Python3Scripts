# coding=utf-8
"""
DATE:   2021/5/18
AUTHOR: Yanxi Li
"""
import json
import os
import random
import time

from urllib.parse import urlparse

'''
IPv4内网地址：

Class A 10.0.0.0-10.255.255.255

默认子网掩码:255.0.0.0

Class B 172.16.0.0-172.31.255.255

默认子网掩码:255.240.0.0

Class C 192.168.0.0-192.168.255.255

默认子网掩码:255.255.0.0
'''

# base data
attack_type = ["异常登录", "系统漏洞攻击", "本地提权", "WEB攻击", "后门控制", "口令爆破", "拒绝服务攻击", "异常登录", "WebShell控制", "WEB扫描", "蠕虫病毒",
               "僵尸网络", "中间人攻击", "应用层扫描", "APT攻击"]

# print(len(attack_type))  # 14

position = ["软件工程师", "Java开发工程师", "PHP开发工程师", "C/C++开发工程师", "Python开发工程师", ".NET开发工程师", "Ruby开发工程师", "Go开发工程师",
            "大数据开发工程师 ", "Hadoop工程师", "爬虫开发工程师", "UI设计师", "视觉设计师", "特效设计师", "仿真应用工程师", "Android开发工程师", "iOS开发工程师",
            "网络安全工程师", "安全研发工程师", "渗透测试工程师", "测试开发工程师", "Web前端开发", "HTML5开发工程师", "机器学习工程师", "深度学习工程师", "图像算法工程师",
            "图像处理工程师", "语音识别工程师", "机器视觉工程师", "算法工程师", "产品经理", "项目经理"]

location = []


def get_random_name():
    family_name = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍郤璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逯盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空丌官司寇仉督子车颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁晋楚闫法汝鄢涂钦段干百里东郭南门呼延归海羊舌微生岳帅缑亢况郈有琴梁丘左丘东门西门商牟佘佴伯赏南宫墨哈谯笪年爱阳佟第五言福百家姓终"
    family_name_list = [i for i in family_name]
    given_name_list = ["平", "军", "可", "海涛", "海波", "海云", "秀英", "伟", "静", "娜", "婷婷", "娟", "敏", "秀兰", "俊杰", "刚", "磊", "洋",
                       "宏伟", "文", "桂英", "智勇", "国栋", "国栋", "国强", "国立", "建业", "志强", "志伟", "志坚", "云天", "云峰", "晓光", "文俊",
                       "振业", "旭", "兰亭", "春秋", "汉华", "汉云", "朝阳", "宗盛", "波", "宁"]
    return random.choice(family_name_list) + random.choice(given_name_list)


def get_random_position():
    """获取随机职业
    """
    return random.choice(position)


def get_random_location():
    """获取随机位置
    """

    with open('./province.json', 'r', encoding='utf-8') as f:
        province_list = json.load(f)

    # print(province_list)
    # random_location_map = [{province['name']:i['name'] for i in province['list'] if "其它" not in i['name']} for province in province_list]

    random_location_list = ["{}{}".format(province['name'], i['name']) for province in province_list for i in
                            province['list'] if "其它" not in i['name']]

    # print(random_location_list)
    return random.choice(random_location_list)


# ip data 避开 IPv4 的范围就行

def get_random_wan_ip():
    """生成随机外网地址
    """
    a = random.randint(11, 171)
    b = random.randint(1, 254)
    c = random.randint(1, 254)
    d = random.randint(1, 254)
    ip = "%d.%d.%d.%d" % (a, b, c, d)

    return ip


def get_random_attack_type():
    """生成随机攻击类型
    """
    return random.choice(attack_type)


def get_random_time():
    """生成随机格式化字符串
    """

    end = int(time.time())
    start = int(time.time()) - 259200

    # print("start时间戳:", start)
    # print("end时间戳:", end)

    # 随机生成格式化日期字符串
    timestamp = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(timestamp)  # 将时间戳生成时间元组
    date_str = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    # print(timestamp)
    # print(date_str)
    return date_str

def get_random_create_time():
    a1 = (2000, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（2000-1-1 00：00：00）
    a2 = (2006, 12, 31, 0, 0, 0, 0, 0, 0)  # 设置结束日期时间元组（2006-12-31 00：00：00）

    start = time.mktime(a1)  # 生成开始时间戳
    # print("start时间戳:", start)
    end = time.mktime(a2)  # 生成结束时间戳
    # print("end时间戳:", end)

    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date_str = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    # print(date_str)
    return date_str


def get_random_title():
    web_info_list = read_json("./website_node_v2.json")
    web_info = random.choice(web_info_list)
    return web_info['title']


def get_domain(url=""):
    """获取域名
    """
    if not url:
        return ""
    else:
        return urlparse(url).netloc


def write_json(config_path, json_obj):
    with open(config_path, 'w', encoding="utf-8") as f:
        f.seek(0)
        f.truncate()
        json.dump(json_obj, f, indent=4)
    print("Write json file in: ", config_path)


def read_json(config_path):
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding="utf-8") as f:
            read_obj = json.load(f)

    return read_obj


_id_count = 0
_id_count_time = int(time.time())


def compute__id():
    global _id_count, _id_count_time

    _id_count += 1

    _id = '{}:{}'.format(_id_count_time, _id_count)

    if time.time() > _id_count_time + 1:
        _id_count = 0
        _id_count_time = int(time.time())
    return _id


if __name__ == '__main__':
    # random_time()
    # write_json("./test.json",{"a":1,"b":2,"c":["x","y","z"]})
    # read_json("./test.json")
    # print(get_random_position())
    # get_random_location()
    # print(get_random_name())
    # get_random_location()
    # print(get_random_title())
    print(get_random_create_time())
