# coding=utf-8
"""
DATE:   2021/5/18
AUTHOR: Yanxi Li
"""

from dev_demo.sec_event_mock.sec_event_data import *


# left data

# 参考sa get_node  注意 node和link      # 生成的json， 参考 graph.json


def gen_graph():
    data = {}

    # 1.获取所有节点，存入node_list


    persons = read_json("./person_node_v5.json")   # 500
    websites = read_json("./website_node_v3.json")

    # persons = read_json("./person_node_v2.json")
    # print(type(persons), persons)
    # websites = read_json("./website_node_v2.json")
    # print(type(websites), websites)

    person_list = []
    web_list = []

    for person in persons:
        p_node = {
            # common
            "id": "P:{}".format(compute__id()),
            "name": person.get('name'),
            "type": "user",
            "ip": person.get('ip'),

            # person 独有
            "gender": person.get('gender'),
            "age": person.get('age'),
            "position": person.get('position'),
            "location": person.get('location'),
            "action": person.get('action'),

            # website 独有
            "domain": "",
            "protocol": "",
            "class": ""
        }

        person_list.append(p_node)

    for web in websites:
        w_node = {
            # common
            "id": "W:{}".format(compute__id()),
            "name": web.get("title"),
            "type": "site",
            "ip": web.get("ip"),

            # person 独有
            "gender": "",
            "age": "",
            "position": "",
            "location": "",
            "action": "",

            # website 独有
            "domain": web.get("domain"),
            "protocol": web.get("protocol"),
            "class": web.get("class"),
            "create_time": web.get("create_time"),
            "record_location": web.get("record_location"),
            "value": web.get("value")
        }
        web_list.append(w_node)

    node_list = person_list + web_list
    # print(node_list)
    # print(len(node_list))  # 219

    # 2.绘制所有连线
    link_list = []

    # debug
    print(len(person_list))
    print(len(web_list))

    # 2.1 绘制 person 访问的 website 连线  每个人都有访问 1-N 个站点

    count_index = len(person_list) // 4
    # 1 person to N Web
    for person in person_list[:count_index]:
        for web in random.sample(web_list, random.randint(5,10)):
            link_d1 = {
                "id": "{}-{}".format(person['id'], web['id']),
                "src": person['id'],  # 连线源，子节点
                "dst": web['id']  # 连线目的，父节点
            }
            link_list.append(link_d1)

    # 1 person to 1 Web
    for person in person_list[count_index:]:
        web = random.choice(web_list)
        link_d2 = {
            "id": "{}-{}".format(person['id'], web['id']),
            "src": person['id'],  # 连线源，子节点
            "dst": web['id']  # 连线目的，父节点
        }
        link_list.append(link_d2)

    # 2.2 绘制 相同 class 的 website 连线
    # 每个class中遍历到的第一个web为dst，其它均为src
    class_list = []
    for web in web_list:
        if web.get("class") and web.get("class") not in class_list:
            class_list.append(web)

    # print("web class list: \n", len(class_list),class_list)

    for w in web_list:
        for c in class_list:
            if w.get("class") == c.get("class") and w.get("id") != c.get("id"):
                link_d3 = {
                    "id": "{}-{}".format(w['id'], c['id']),
                    "src": w['id'],  # 连线源，子节点
                    "dst": c['id']  # 连线目的，父节点
                }
                link_list.append(link_d3)

    # 3.组装好数据，写入json
    data = {
        "nodes": node_list,
        "nodes_num": len(node_list),
        "links": link_list,
        "links_num": len(link_list)
    }

    # print(data)

    write_json("./graph_data_{}.json".format(int(time.time())), data)


if __name__ == '__main__':
    gen_graph()
