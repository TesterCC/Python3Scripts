# coding=utf-8
"""
DATE:   2022/1/11
AUTHOR: TesterCC
"""

"""
阿里云API市场
https://market.aliyun.com/products/?spm=5176.78296.J_8396760290.23.39275d769hLGQL&keyword=ip%E6%9F%A5%E8%AF%A2

# 有region的用region
# 12000*2 = 24000条数据，写文件备用
"""
import time
import requests
import random

uas = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
]


def get_ip_geo_by_api(ip: str):
    # headers =  {"Authorization":"APPCODE 1349a162fcb44646a6be28d9add1bf93",
    #             "Host":"api01.aliyun.venuscn.com","Content-Type":"application/json; charset=utf-8"}

    # headers = {"Authorization": "APPCODE 1349a162fcb44646a6be28d9add1bf93",
    #            "Content-Type": "application/json; charset=utf-8",
    #            "User-Agent": random.choice(uas)}

    headers = {"Authorization": "APPCODE 1349a162fcb44646a6be28d9add1bf93",
               "Content-Type": "application/json; charset=utf-8"}

    TARGET_URL = f"http://api01.aliyun.venuscn.com/ip?ip={ip}"

    ret = requests.get(TARGET_URL, headers=headers, timeout=5)

    if ret.status_code == 200:
        resp = ret.json()
        # print(resp)
        # print(resp.get('data'))
        # print("region", resp.get('data').get('region'))
        # print("country", resp.get('data').get('country'))
        # print("city", resp.get('data').get('city'))
        if resp.get('data').get('region'):
            # print("region", resp.get('data').get('region'))
            return resp.get('data').get('region')
        else:
            return "-"
    else:
        return "-"


def ip2geo():
    with open("./gen_cip.txt") as f:
        ip_list = f.readlines()

    ip_list = [ip.replace("\n", "") for ip in ip_list]
    # print(len(ip_list))
    # print(ip_list)

    with open(f"ip_geo_map_{int(time.time())}.txt", "w", encoding="utf-8") as f:
        for ip in ip_list[21328:]:
            ip_geo = get_ip_geo_by_api(ip)
            print(ip, ip_geo)
            f.write(ip + "," + ip_geo + "\n")


if __name__ == '__main__':
    # # get_ip_geo_by_api("38.233.9.29")
    # get_ip_geo_by_api("171.212.241.100")
    ip2geo()
