#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-01 23:36'


import requests
import time
from openpyxl import Workbook

"""
用的别人现成的脚本，可优化方向：
1.多线程
2.UA变更
3.IP替换
主要是查询出访问限制是限制的IP还是UA
"""

def query(kkxs,terms="2018-2019-2-1"):
    '''
    :param kkxs:学院编号
    :param terms: 学期号，默认2018-2019-2-1,terms格式为2018-2019-2-1
    :return:每个学院返回的课表数据
    '''
    time.sleep(5)       #防止请求频率过高
    datalist = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    url = "http://zhjwjs.scu.edu.cn/teacher/personalSenate/giveLessonInfo/thisSemesterClassSchedule/getCourseArragementPublic"
    postdata = {
        "zxjxjhh":terms,  #学期,默认是18-19第二学期
        "kch": "",  # 课程号
        "kcm": "",  # 课程名
        "js": "",  # 教师
        "kkxs": kkxs,  # 开课院系
        "skxq": "",  # 上课星期
        "skjc": "",  # 上课节次
        "xq": "",  # 校区
        "jxl": "",  # 教学楼
        "jas": "",  # 教室
        "pageNum": "1",  # 显示的页数
        "pageSize": "30",  # 每页的课程数
        "kclb": ""  # 课程类别
    }
    r = requests.post(url=url, data=postdata, headers=headers)
    m = r.json()["list"]
    totalcourse = m["pageContext"]["totalCount"]  # 总课数
    page = totalcourse / 30 + 1
    while int(postdata["pageNum"]) <= page:  # 存储数据到list
        currentpage = int(postdata["pageNum"])
        for i in r.json()["list"]["records"]:
            datalist.append(i)
        currentpage += 1
        postdata["pageNum"] = str(currentpage)
        r = requests.post(url=url, data=postdata, headers=headers)

    return datalist

def save_to_excel():
    '''
    保存数据为excel
    :return:
    '''
    wb = Workbook()
    ws = wb.active
    ws.append(["课程号", "课序号", "课程名", "学分", "开课院系", "上课教师", "选课限制",
               "校区", "上课教室", "上课星期", "周次", "教学楼", "上课节次"])
    collogeDic = {'101': '艺术学院', '102': '经济学院', '103': '法学院', '104': '文学与新闻学院', '105': '外国语学院', '106': '历史文化学院（旅游学院）',
                  '107': '马克思主义学院', '108': '国际关系学院', '201': '数学学院', '202': '物理科学与技术学院（核科学与工程技术学院）', '203': '化学学院',
                  '204': '生命科学学院', '205': '电子信息学院', '300': '高分子科学与工程学院', '301': '材料科学与工程学院', '302': '制造科学与工程学院',
                  '303': '电气信息学院', '304': '计算机学院', '305': '建筑与环境学院', '306': '水利水电学院', '308': '化学工程学院', '309': '轻纺与食品学院',
                  '311': '软件学院', '312': '四川大学匹兹堡学院', '313': '空天科学与工程学院', '314': '网络空间安全学院', '401': '公共管理学院',
                  '402': '商学院', '403': '灾后重建与管理学院', '501': '华西基础医学与法医学院', '502': '华西临床医学院', '503': '华西口腔医学院',
                  '504': '华西公共卫生学院', '505': '华西药学院', '506': '华西动物中心', '601': '联合班', '603': '吴玉章学院',
                  '604': '生物治疗国家重点实验室', '700': '研究生院', '888': '体育学院', '900': '党委武装部（军事教研室）', '901': '网络教育学院',
                  '902': '图书馆', '903': '分析测试中心', '904': '工程设计中心', '905': '工程训练中心', '906': '电子实习中心', '907': '电工电子中心',
                  '908': '化学基础实验教学中心', '909': '计算机基础教学实验中心', '910': '招生就业处', '911': '校团委', '912': '心理健康教育中心',
                  '913': '国家大学科技园', '914': '海外教育学院', '915': '国际合作与交流处', '918': '实验室及设备管理处', '919': '现代教育技术中心',
                  '920': 'IBM技术中心', '925': '文化科技协同创新研发中心', '929': '出国留学人员培训部', '932': '中国西部边疆安全与发展协同创新中心',
                  '993': '成都美国留学中心', '997': '创新教育', '998': '党委学生工作部（处）', '999': '其它'}   #学院数据

    # simple one
    # collogeDic = {'304': '计算机学院', '311': '软件学院', '314': '网络空间安全学院', '700': '研究生院'}  # 学院数据

    for colloge_id in collogeDic:
        response_course = query(colloge_id)
        for each_course in response_course:
            kch = each_course['kch']  # 课程号
            kxh = each_course['kxh']  # 课序号
            kcm = each_course['kcm']  # 课程名
            xf = each_course['xf']  # 学分
            kkxsjc = each_course['kkxsjc']  # 开课院系
            skjs = each_course['skjs']  # 上课教师
            xkxzsm = each_course['xkxzsm'].strip()  # 选课限制说明
            kkxqm = each_course['kkxqm']  # 校区
            jash = each_course['jash']  # 上课教室
            skxq = each_course['skxq']  # 上课星期
            zcsm = each_course['zcsm']  # 周次
            jxlm = each_course['jxlm']  # 教学楼
            if (each_course['skjc'] != None):
                jieci = str(each_course['skjc']) + "-" + str(each_course['skjc'] + each_course['cxjc'] - 1)  # 上课节次
            else:
                jieci = None
            ws.append([kch, kxh, kcm, xf, kkxsjc, skjs, xkxzsm, kkxqm, jash, skxq, zcsm, jxlm, jieci])
        print("%s数据已完成"%collogeDic[colloge_id])
    wb.save('course.xlsx')

if __name__=="__main__":
    save_to_excel()