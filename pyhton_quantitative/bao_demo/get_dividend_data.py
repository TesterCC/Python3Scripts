# -*- coding: utf-8 -*-
# @Time    : 2023/1/21
# @Author  : SecCodeCat


import baostock as bs
import pandas as pd
import numpy as np
import datetime
import math_demo
import pickle

#  https://zhuanlan.zhihu.com/p/43690156

def get_bonus_info_from_bs():
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    # 获得最新所有的股票代码  # todo
    allstocksinfo = get_all_stockcode_info()
    #     print(type(allstocksinfo),allstocksinfo)
    bonus_info_dict = {}

    for stockcode in allstocksinfo.keys():
        if allstocksinfo[stockcode] > "2008-01-01":
            continue
        bonus_info_dict[stockcode] = []
        for yearadd in range(10):
            year = "%d" % (2008 + yearadd)
            rs_dividend = bs.query_dividend_data(stockcode, year, yearType="report")
            data_list = []
            while (rs_dividend.error_code == '0') & rs_dividend.next():
                data_list.append(rs_dividend.get_row_data())
            result_dividend = pd.DataFrame(data_list, columns=rs_dividend.fields)
            result_dividend = result_dividend[
                ['dividPlanDate', 'dividOperateDate', 'dividCashPsBeforeTax', 'dividStocksPs']]

            print(result_dividend.empty, result_dividend.size, result_dividend)
            if not result_dividend.empty and len(result_dividend.index) > 0 and result_dividend.size > 0:
                for i in result_dividend.index:
                    print(result_dividend.size)
                    print(result_dividend.ix[i, :])
                    print(list(result_dividend.ix[i, :]))
                    bonus_info_dict[stockcode].append(list(result_dividend.ix[i, :]))
    #         break

    whandle = open('../data/bonus_info.txt', 'wb')
    pickle.dump(bonus_info_dict, whandle)
    whandle.close()

    bs.logout()


def select_stock_by_bonys():
    rhandle = open('../data/bonus_info.txt', 'rb')
    bonus_info_dict = pickle.load(rhandle)
    rhandle.close()

    dividend_times_dict = []
    for stockcode in bonus_info_dict.keys():
        dividend_times_dict.append([stockcode, len(bonus_info_dict[stockcode])])

    #     sorted(dividend_times_dict,key = labmda x:x[1],reversed = True)
    sortedlist = sorted(dividend_times_dict, key=lambda one: one[1], reverse=True)


    priorlist = [info[0] for info in sortedlist]
    # get_code_name自己定义的函数，返回股票代码和名称的dict.
    stockinfo = get_code_name()
    for i in range(20):
        db_code = priorlist[i]
        stockcode = '%s.%s' % (db_code[3:], db_code[:2].upper())
        if stockcode in stockinfo:
            print("%s,%s" % (stockcode, stockinfo[stockcode])),
        else:
            print(stockcode)