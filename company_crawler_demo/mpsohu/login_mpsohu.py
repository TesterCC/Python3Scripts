#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/2 21:48'

"""
每个账号每天发5篇，无需换IP发布，但需清除cookie，发布间隔3分钟。
发布方式
http://mp.sohu.com/v2/main/news/add.action
"""

import logging
import unittest

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import requests

LOGIN_URL = "https://mp.sohu.com/mpfe/v3/login"
AFTER_LOGIN_URL = "https://mp.sohu.com/mpfe/v3/main/first/page"

EDIT_ARTICLE_URL = "http://mp.sohu.com/v2/main/news/add.action"

USERNAME = "18702895635"  # [18702895635, 15281005385, 18683715921, 18782291154, 18108061758]
PASSWORD = ""


def mpsohu_sender(url=LOGIN_URL, username=USERNAME, password=PASSWORD):
    # driver = webdriver.PhantomJS()
    driver = webdriver.Chrome()

    driver.get(url)

    login_nav = driver.find_element_by_xpath('//*[@id="mpfe"]/div[3]/div/article/div[1]/div[2]/div/div[1]/span[1]')

    login_nav.click()

    input_username = driver.find_element_by_xpath(
        "//*[@id='mpfe']/div[3]/div/article/div[1]/div[2]/div/div[3]/div[1]/input")

    input_username.click()

    input_username.send_keys(username)

    input_password = driver.find_element_by_xpath(
        "//*[@id='mpfe']/div[3]/div/article/div[1]/div[2]/div/div[3]/div[2]/input")

    input_password.click()

    input_password.send_keys(password)

    submit = driver.find_element_by_xpath('//*[@id="mpfe"]/div[3]/div/article/div[1]/div[2]/div/button')

    submit.click()

    sleep(5)

    print(driver.current_url)

    after_login_url = AFTER_LOGIN_URL
    if driver.current_url == after_login_url:
        print("Login Success!")

        # Get and Save cookie
        Cookies = driver.get_cookies()
        print("Cookie:\n{}".format(Cookies))
        # print("Clear cookie...")
        # driver.delete_all_cookies()
        # print("Cookie:\n{}".format(driver.get_cookies()))

        import os
        cookie_path = os.getcwd() + "/cookies/mpsohu/"
        cookie_dict = {}
        import pickle
        for cookie in Cookies:
            # 写入文件
            # f = open('G:/scrapy/ArticleSpider/cookies/zhihu/' + cookie['name'] + '.zhihu', 'wb')
            f = open(cookie_path + cookie['name'] + '.mpsohu', 'wb')
            pickle.dump(cookie, f)
            f.close()
            cookie_dict[cookie['name']] = cookie['value']

        # jump to edit article page
        # driver.get(EDIT_ARTICLE_URL)
        sleep(3)
        # driver.quit()

        s = requests.Session()
        for cookie in Cookies:
            s.cookies.set(cookie['name'], cookie['value'])

        # 加正常UserAgent, 应对反爬虫策略
        UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"

        # header = {
        #           "User-Agent": UA,
        #           # "Referer": "http://www.v2ex.com/signin"
        #           }

        header = s.headers.update({"User-Agent": UA})
        # print(s.headers)

        # 访问写文章界面
        response = s.get(EDIT_ARTICLE_URL)
        # bodyStr = response.text
        # print(bodyStr)   # return html
        print(response.status_code)

        # 尝试发表文章

        post_draft_url = "https://mp.sohu.com/v3/news/draft"
        publish_direct_url = "https://mp.sohu.com/v3/news/publish"

        content_message = '''<p>会议即将召开，<strong>第8届中国网络安全大会（NSC 8888）</strong>详情请上活动家官网查看。</p><p>会议网址：</p><p>https://www.huodongjia.com/event-1130102179.html</p><p>（请将网址复制到浏览器中打开）</p><p>CMAC简介</p><p>随着Medical Driven时代的来临，医药行业新政频出，行业正在发生巨变,企业面临诸多挑战，医药企业如何快速适应新趋势？如何成功转型？学术营销是药企未来唯一出路。</p><p>CMAC（Chinese Medical Affairs Conference）即中华医学事务年会于2015年创立，由石成医学主办，得到了RDPAC MA工作组大力支持，目前已成为医学事务领域规模最大、最高端的行业年会，年参会规模已经超过1500人。截止目前已经成功举办两届，共四场大会（一届年会分为两场，MNCs专场和国内药企专场）。CMAC已经成为名副其实的医学事务第一平台。2018年“第三届中华医学事务年会之智慧医学 数据先行”即将启动，敬请期待。</p><p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180403/c9131cbf80f14400bdc600433fc8b1f7.jpeg" max-width="600"></p><p>往期精彩回顾：</p><p>2016年4月5-7日第一届中华医学事务年会（CMAC)在北京召开。议主题：医学驱动引领新时代。会议规模500余人，首次亮相就创造了医学事务历史上的一次奇迹。行业发展平台助力。</p><p>2016年9月2-3日第一届中华医学事务年会(CMAC)之国内药企专场在南京召开，会议主题：医学助力药企转型，会议规模300余人，第一次中国本土药企有了自己的医学事务行业年会，同样也是一个标记史册的里程碑事件，加速了本土药企学术化转型。</p><p>2017年4月6-8日第二届中华医学事务年会(CMAC)在北京召开，主题：智慧医学 制胜全局。会议内容丰富多彩，引领新思维。会议规模又一次创造了历史，超过了700人。CMAC作为医学事务领域的第一平台，影响力不断扩大。</p><p>2017年9月1-2日第二届中华医学事务年会(CMAC)之国内药企专场在上海召开，主题：洞见医学之数据为王。会议规模超过400余人，参会企业超过120家，CMAC平台见证了行业的快速发展。</p><p>除此之外，以CMAC平台为依托，应广大医学事务同仁的强烈要求，还成功举办了多次研讨班和专题讲座，获得了非常好的反响。</p><p><strong>会议嘉宾</strong></p><p>CMAC，诚挚邀请医学事务、市场、销售、政府事务等同仁积极加入，共谋中国医学事务的美好明天！</p><p><strong><span style="font-size: 20px;">会议日程</span></strong></p><p style="text-align: center;"><img src="//5b0988e595225.cdn.sohucs.com/images/20180403/25cec598efc84ca0ae870df5fd0d50ad.jpeg" max-width="600"></p><p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180326/4ad8e52fab2e4552bb107d5bdb7bf1c9.jpeg" max-width="600"></p><p>立即报名：</p><p>https://www.huodongjia.com/event-1130102179.html</p><p>更多<strong>医疗管理</strong><strong>智慧医疗</strong>会议（这里是调用当前会议的所有tag标签，中间用空格分别隔开）尽在活动家，欢迎使用活动家小程序查询报名会议，微信搜索“活动家会议”</p>'''

        print("Start to test save draft, and get article id")

        post_data = {
            'title': '第Test届中国活动家大会（0000）【活动家】',
            'brief': '',
            'content': content_message,
            'channelId': 24,
            'categoryId': 70,
            # 'id': 227155152,  no need when 1st
            'userColumnId': 119129,
            'isOriginal': 0
        }

        # Save Draft
        # req = s.post(post_draft_url, data=post_data, headers=header)
        #
        # article_id = req.text
        # print("Article id is {}".format(article_id))

        post_data2 = {
            'title': '第77届中国活动家大会【活动家】',
            'brief': '',
            'content': content_message,
            'channelId': 24,  # need map
            'categoryId': 70,  # need map
            # 'id': 227155152,
            # 'userColumnId': 119129,
            # 'isOriginal': 0
        }

        # Publish article directly
        print("Start to test directly send.")
        req = s.post(publish_direct_url, data=post_data2, headers=header)
        article_id = req.text
        print("Article id is {}".format(article_id))
        print("{0}".format(req.status_code))

        # Article Check
        """
        https://mp.sohu.com/v2/main/news/preview_by_id.action?id=227181850   发布后立刻可以获得的link
        https://mp.sohu.com/v2/main/news/edit.action?id=227181850
        https://www.sohu.com/a/227181850_134221    正式发表成功的link

        https://www.sohu.com/a/227231697_134221    
        https://mp.sohu.com/v2/main/news/preview_by_id.action?id=227231697
        """

        print("TEST END >>>>>>>")

    else:
        print("Current url is incorrect!")
        driver.quit()


if __name__ == '__main__':
    mpsohu_sender(username='18702895635', password='huodongjia123456')










