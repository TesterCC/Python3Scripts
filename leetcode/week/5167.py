#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-25 10:31'

"""
如果出现下述两种情况，交易 可能无效：

交易金额超过 ¥1000
或者，它和另一个城市中同名的另一笔交易相隔不超过 60 分钟（包含 60 分钟整）
每个交易字符串 transactions[i] 由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。

给你一份交易清单 transactions，返回可能无效的交易列表。你可以按任何顺序返回答案。
"""


# class Solution:
#     def invalidTransactions(self, transactions):
#         ret = []
#         for i in range(len(transactions)-1):
#             name,time,amount,city = transactions[i].split(",")
#             name2,time2,amount2,city2 = transactions[i+1].split(",")
#
#             if abs(int(amount) - int(amount2)) > 1000:
#                 ret = transactions[i + 1]
#
#             if name == name2:
#                 if abs(int(time) - int(time2)) <= 60:
#                     ret = transactions[i + 1]
#
#             if city == city2:
#                 if abs(int(time) - int(time2)) <= 60:
#                     ret = transactions[i + 1]
#         return ret

class Solution:
    def invalidTransactions(self, transactions: [str]) -> [str]:

        name0, time0, amount0, city0 = transactions[0].split(",")

        ret = list()

        for i in range(1, len(transactions)):

            name, time, amount, city = transactions[i].split(",")

            if abs(int(amount) - int(amount0)) > 1000:
                ret.append(transactions[i])

            elif city == city0:
                if abs(int(time) - int(time0)) <= 60:
                    ret.append(transactions[i])
            else:
                if abs(int(time) - int(time0)) <= 60:
                    ret.append(transactions[0])
                    ret.append(transactions[i])

        return ret


if __name__ == '__main__':
    so = Solution()
    # {name},{time},{amount},{city}
    transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]
    transactions2 = ["alice,20,800,mtv", "alice,50,1200,mtv"]
    transactions3 = ["alice,20,800,mtv", "bob,50,1200,mtv"]

    transactions4 = ["alice,20,800,mtv", "alice,50,100,beijing"]
    transactions5 = ["alex,676,260,bangkok","bob,656,1366,bangkok","alex,393,616,bangkok","bob,820,990,amsterdam","alex,596,1390,amsterdam"]

    transactions6 = ["bob,689,1910,barcelona", "alex,696,122,bangkok", "bob,832,1726,barcelona", "bob,820,596,bangkok",
     "chalicefy,217,669,barcelona", "bob,175,221,amsterdam"]

    ret1 = so.invalidTransactions(transactions)
    ret2 = so.invalidTransactions(transactions2)
    ret3 = so.invalidTransactions(transactions3)
    ret4 = so.invalidTransactions(transactions4)
    ret5 = so.invalidTransactions(transactions5)
    ret6 = so.invalidTransactions(transactions6)
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    print(ret5)
    print(ret6)