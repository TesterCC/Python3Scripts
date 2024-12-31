# coding=utf-8
"""
DATE:   2022/1/11
AUTHOR: TesterCC
"""

"""
根据IP查询对应地理位置  不行，名字因为不符合需求

# pip install geoip2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip python-geoip-geolite2 -i https://pypi.tuna.tsinghua.edu.cn/simple

geo db:
https://raw.githubusercontent.com/wp-statistics/GeoLite2-City/master/GeoLite2-City.mmdb.gz

https://pypi.org/project/geoip2/
"""

import geoip2.database

reader = geoip2.database.Reader('./GeoLite2-City.mmdb')

def get_ip_geo(ip:str):
    ret = reader.city(ip)
    print("IP Address: ", ip)
    print("Country:", ret.country.name)
    print("Subdivisions: ", ret.subdivisions.most_specific.name)
    print("City: ", ret.city.name)
    print("Latitude: ", ret.location.latitude)
    print("Longitude: ", ret.location.longitude)


if __name__ == '__main__':
    # get_ip_location("127.0.0.1")
    get_ip_geo("133.23.44.199")
    print("--"*20)
    get_ip_geo("171.212.241.100")