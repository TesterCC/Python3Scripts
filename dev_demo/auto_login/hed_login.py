#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import os

# login whoeton

# install firefox driver, selenium python3 client
# run as Administrator, and manual set system environment vars
username = os.environ.get("HNAME")
password = os.environ.get("HPASSWD")
server = os.environ.get("HHOST")


def open_network():
    url = f"http://{server}/login"

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    # print(driver.page_source)
    el_username = driver.find_element(By.NAME, 'param[UserName]')  # Find the search box

    el_username.send_keys(username)
    el_password = driver.find_element(By.NAME, 'param[UserPswd]')  # Find the search box

    el_password.send_keys(password)
    el_login_btn = driver.find_element(By.ID, 'btn_login')
    el_login_btn.click()

    cur_window_handle = driver.current_window_handle
    print(cur_window_handle)
    print(driver.current_url)
    window_handles_list = driver.window_handles
    print(f"[D] window_handles_list: {window_handles_list}")

    # driver.minimize_window()
    browser_cookie = driver.get_cookies()
    print(f"get cookies info: \n{browser_cookie}")

    for item in browser_cookie:
        if item.get('expiry'):
            delta_time = item.get('expiry') - int(time.time())
            print(f"[D] {delta_time} second expired")
        if item.get('fms_session'):
            print(f"[D] fms_session: {item.get('fms_session')}")

    # for wh in window_handles_list:
    #     tmp_dict = dict()
    #     tmp_dict[wh] = driver.current_url
    #     print(tmp_dict)
    #     if wh != cur_window_handle:
    #         driver.switch_to.window(wh)
    #         driver.close()
    #         driver.switch_to.window(cur_window_handle)
    # # driver.quit()


if __name__ == '__main__':

    while True:
        open_network()
        time.sleep(3600 * 3)
        # https://zohead.com/archives/wholeton-linux-client/
        # 看起来也可以通过ws带fms_session不断刷新（方式相对优雅），不过实现上每隔固定时间直接重新登录一次更简易。