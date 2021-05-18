# coding=utf-8
"""
DATE:   2021/5/18
AUTHOR: Yanxi Li
"""


from dev_demo.sec_event_mock.sec_event_data import *



def gen_person_node_json(count=100):

    ret = []

    for i in range(count):
        data = {
            "name": get_random_name(),
            "gender": random.choice(["男","女"]),
            "age": "{}".format(random.randint(20,50)),
            "position": get_random_position(),
            "ip": get_random_wan_ip(),
            "location": get_random_location(),
            "action": random.choice(["visit","attack"])
        }

        ret.append(data)

    # print(ret)
    write_json("./person_node_v2.json", ret)

if __name__ == '__main__':
    gen_person_node_json(count=200)
    # print(read_json("./person_node.json"))