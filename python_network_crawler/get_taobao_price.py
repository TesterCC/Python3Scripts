#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/31 17:27'

from selenium import webdriver
from bs4 import BeautifulSoup



# Step 1 -- Get Ajax Html with Selenium
driver = webdriver.Chrome(executable_path="chromedriver")     # 填写Chromedriver的路径, 如果已经将其加入环境变量，则要填"chromedriver"
# chromedriver -h
# chromedriver --version

target_url = "https://detail.tmall.com/item.htm?spm=a222t.8063993.4954155005.6.6209da3bxorZJa&acm=lb-zebra-164656-978614.1003.4.2269880&id=559791372740&scm=1003.4.lb-zebra-164656-978614.ITEM_559791372740_2269880&sku_properties=5919063:6536025;122216431:27772"

driver.get(target_url)

# print(driver.page_source)  # for debug

# Step 2 -- Extract needed data
soup = BeautifulSoup(driver.page_source, "html.parser")  # 这个是python3.5自带的网页解析器
price = soup.find("span", class_="tm-price").text.strip()
print("Good Price is %s" % price)

# Step 3 -- Store data
# with open('price.txt', "a+") as f:
#     f.write(price)
#     f.close()


driver.quit()