#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-24 13:32'

import time
from ObserverModel import Observable, Observer    # IDE报错，但命令行执行可导入，不影响


class Account(Observable):
    """User Account"""

    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        # print(region)   # 美国洛杉矶
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        # 由IP地址获取地区信息（模拟）。真实项目中应该调用IP地址解析服务
        ipRegions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        # 计算本次登录与最近几次登录的地区差距
        # 本例仅简单地用字符串匹配来模拟，真实的项目中应该调用地理信息相关的服务（接口）
        latestRegion = self.__latestRegion.get(name)
        #print(latestRegion)
        #print(latestRegion is not None and latestRegion != region)
        return latestRegion is not None and latestRegion != region


class SmsSender(Observer):
    """短信发送器"""

    def update(self, observable, object):
        def update(self, observable, object):
            print("[短信发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
                  + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
                  + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))

class MailSender(Observer):
    """邮件发送器"""

    def update(self, observable, object):
        print("[邮件发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


def testTime():
    print(time.time())
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
    print(strTime)

def testLogin():
    account = Account()
    account.addObserver(SmsSender())
    account.addObserver(MailSender())
    account.login("Alice", "101.47.18.9", time.time())
    account.login("Alice", "67.218.147.69", time.time())


# testTime()
testLogin()
