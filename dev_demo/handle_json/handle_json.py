# -*- coding=utf-8 -*-
import json
import os
import time


# /opt/ips

class JsonChecker:

    # deprecated, use new method
    @staticmethod
    def check_json(check_path="./ips"):
        # 1. check [node_id].txt in specific dir
        # 2. if txt exist, read info and trans to dict

        if os.path.exists(check_path):
            dir_data = os.listdir(check_path)
            # print(dir_data)  #  debug ['192.168.1.1.txt', '192.168.1.2.txt', '192.168.1.3.txt']
            file_list = [f for f in dir_data if f.endswith(".txt")]

            data = []
            print(f"[D] file_list: {file_list}")  # debug
            for file in file_list:
                json_file_path = f"{check_path}/{file}"
                with open(json_file_path) as f:
                    for line in f:
                        # parse every line to dict
                        line_data = json.loads(line)
                        data.append(line_data)

            updated_data = [{'sip': item['src_addr'], 'sport': item['src_port'], 'dip': item['dst_addr'],
                             'dport': item['dst_port'], 'protocol': item['protocol']} for item in data]
            print(f"[D] txt all json data: {data}")
            print(f"[D] replace json data: {updated_data}")

    # @staticmethod
    # def json_info_monitor():
    #     interval_time = 3  # unit second
    #     max_count = 86400
    #     check_path = "/opt/json_info"  # custom
    #     count = 0  # for debug
    #
    #     while True:
    #         JsonChecker.check_json(check_path)
    #         time.sleep(interval_time)
    #         count += 1
    #         if count >= max_count: count = 0  # for debug
    #         print(f"[*] run {count} times...")  # for debug


if __name__ == '__main__':
    json_checker = JsonChecker()
    json_checker.check_json(check_path="./ips")
