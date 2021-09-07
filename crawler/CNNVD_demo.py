# coding=utf-8
"""
DATE:   2021/9/7
AUTHOR: TesterCC
"""
############################
# 现有需求是给了一坨CVE编号
# 通过编号在CNNVD精准爬取详情
# 如需漏洞名称 和 补丁之类的
# 直接提取xpath，然后写逻辑就行
############################

import re
import time
import requests
import xlrd
from xlutils.copy import copy
from lxml import etree

REQ_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,zh-TW;q=0.6,und;q=0.5,uk;q=0.4,ja;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '177',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'SESSION=b13f18be-0951-4572-9bac-e3aebff9361b; topcookie=a1',
    'DNT': '1',
    'Host': 'cnnvd.org.cn',
    'Origin': 'http://cnnvd.org.cn',
    'Referer': 'http://cnnvd.org.cn/web/xxk/ldxqById.tag?CNNVD=CNNVD-202012-602',
    'sec-gpc': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
}

POST_DATAS = {
    'CSRFToken': "",
    'cvHazardRating': "",
    'cvVultype': "",
    'qstartdateXq': "",
    'cvUsedStyle': "",
    'cvCnnvdUpdatedateXq': "",
    'cpvendor': "",
    'relLdKey': "",
    'hotLd': "",
    'isArea': "",
    'qcvCname': "",
    'qcvCnnvdid': "",
    'qstartdate': "",
    'qenddate': "",
}


def write_data_to_xls(cve_num, cve_tags, cve_info):
    cve_data = [[cve_num, cve_tags, cve_info]]
    index = len(cve_data)
    workbook = xlrd.open_workbook("CVE.xls")
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rows_old = worksheet.nrows
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    for i in range(0, index):
        for j in range(0, len(cve_data[i])):
            new_worksheet.write(i + rows_old, j, cve_data[i][j])
    new_workbook.save("CVE.xls")
    print(">>> xls格式表格【追加】写入！\n")


def search_cve(cve_num):
    search_cve_url = "http://cnnvd.org.cn/web/vulnerability/queryLds.tag"

    POST_DATAS['qcvCnnvdid'] = cve_num
    REQ_HEADERS['Content-Length'] = '177'
    REQ_HEADERS['Origin'] = 'http://cnnvd.org.cn'

    req = requests.post(search_cve_url, headers=REQ_HEADERS, data=POST_DATAS, timeout=6)
    html = etree.HTML(req.text)
    cve_xpath = html.xpath('//*[@id="vulner_0"]/a/@href')

    if cve_xpath:
        return cve_xpath[0]
    else:
        return False


def extract_cve_tags_version(cve_info):
    cve_tags_data = re.findall("受到影响：(\S+.*)", cve_info)

    if cve_tags_data:
        cve_tags_data = cve_tags_data[0]
        print("影响范围：" + cve_tags_data[0:8] + "... ...")
    else:
        cve_tags_data = re.findall(".*。(\S+.*)存在.*", cve_info)
        cve_tags_data = cve_tags_data[0]
        print("影响范围：" + cve_tags_data)

    tmp_info_data = re.findall("目前尚无此漏洞的相关信息", cve_info)
    if tmp_info_data:
        cve_info_data = "细节未披露"
        print("漏洞描述：" + cve_info_data)
    else:
        cve_info_data = cve_info
        print("漏洞描述：" + cve_info[0:8] + "... ...")

    return cve_tags_data, cve_info_data


def get_cve_result(cve_num):
    cnnvd_url = search_cve(cve_num)

    if cnnvd_url:
        cve_xpath_url = 'http://cnnvd.org.cn' + cnnvd_url
        print("爬取网址：" + cve_xpath_url)
        try:
            del REQ_HEADERS['Content-Length']
            del REQ_HEADERS['Origin']
        except Exception as e:
            pass
        time.sleep(2)
        try:
            req = requests.get(cve_xpath_url, headers=REQ_HEADERS, timeout=6)
        except Exception as e:
            time.sleep(5)
            get_cve_result(cve_num, cnnvd_url)

        html = etree.HTML(req.text)
        cve_info_xpath = html.xpath('/html/body/div[4]/div/div[1]/div[3]/p')

        tmp_info_data = ""
        for i in cve_info_xpath:
            tmp_data = i.text
            tmp_data = re.search("(\S+.*)", tmp_data)
            if tmp_data:
                tmp_data = "".join(tmp_data.group())
                tmp_info_data += tmp_data

        cve_tags_data, cve_info_data = extract_cve_tags_version(tmp_info_data)
    else:
        cve_tags_data = ""
        cve_info_data = "细节未披露"
        print("CNNVD无此CVE数据！")
    write_data_to_xls(cve_num, cve_tags_data, cve_info_data)


def read_cve_num():
    with open('./cve_num.txt', 'r') as f:
        tmp_cve_num = f.readlines()
        for i in tmp_cve_num:
            i = i.rstrip('\n')
            print("漏洞编号：" + i)
            time.sleep(3)
            get_cve_result(i)


if __name__ == '__main__':
    read_cve_num()
