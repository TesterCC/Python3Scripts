# coding=utf-8
'''
DATE: 2020/09/17
AUTHOR: Yanxi Li
'''

# prepare for interface testing
import re


# 本地接口测试路径和线上接口测试路径有差异，写个批量替换函数
def change_host(url_list: list, pattern: str, host: str) -> list:
    """
    精准匹配
    """
    if len(url_list) == 0 or pattern == '':
        raise AttributeError
    return [re.sub(pattern, host, i) for i in url_list]


if __name__ == '__main__':
    input_url_list = [
        "http://10.0.4.141:8700/add_service/?ip=10.0.0.8&protocol=TCP&port=1433",
        "http://10.0.4.141:8700/add_service/?ip=10.0.0.9&protocol=TCP&port=1433&monitor=true",
        "http://10.0.4.141:8700/add_service/?ip=10.0.0.12&protocol=TCP&port=1433&monitor=false&offline=true",
        "http://10.0.4.141:8700/add_service/?ip=10.0.0.13&port=3307&monitor=true&offline=true"
    ]
    ret = change_host(input_url_list, "10.0.4.141:8700/", "10.0.0.115/asset_api/")
    print(ret)
