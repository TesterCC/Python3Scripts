# 导入函数库
# group shared quantitative strategy
from jqdata import *

import numpy as np
import pandas as pd
import math


# 初始化函数
def initialize(context):
    # 设定基准, 指定为纳指
    set_benchmark('513100.XSHG')
    # 用真实价格交易
    set_option('use_real_price', True)
    # 打开防未来函数
    set_option("avoid_future_data", True)
    # 设置滑点
    set_slippage(FixedSlippage(0.001))
    # 设置交易成本
    set_order_cost(
        OrderCost(open_tax=0, close_tax=0, open_commission=0.0001, close_commission=0.0001, close_today_commission=0,
                  min_commission=0), type='fund')
    # 过滤一定级别的日志
    log.set_level('system', 'error')
    # 参数
    g.etf_pool = [
        '518880.XSHG',  # 黄金ETF（大宗商品）
        '513100.XSHG',  # 纳指100（海外资产）
        '159915.XSHE',  # 创业板100（成长股，科技股，中小盘）
        '510300.XSHG',  # 沪深300（价值股，蓝筹股，大盘）
        '588080.XSHG',  # 科创板50 （科创股）
    ]
    g.m_days = 25  # 动量参考天数  24 or 25
    # 每天 9:50 执行卖出操作
    run_daily(sell, '9:50')
    # 每天 9:51 执行买入操作
    run_daily(buy, '9:51')


# 基于年化收益和判定系数打分的动量因子轮动
def get_rank(etf_pool):
    score_list = []
    for etf in etf_pool:
        df = attribute_history(etf, g.m_days, '1d', ['close'])
        y = df['log'] = np.log(df.close)
        x = df['num'] = np.arange(df.log.size)
        slope, intercept = np.polyfit(x, y, 1)
        annualized_returns = math.pow(math.exp(slope), 250) - 1
        r_squared = 1 - (sum((y - (slope * x + intercept)) ** 2) / ((len(y) - 1) * np.var(y, ddof=1)))
        score = annualized_returns * r_squared
        score_list.append(score)
    df = pd.DataFrame(index=etf_pool, data={'score': score_list})
    df = df.sort_values(by='score', ascending=False)
    rank_list = list(df.index)

    # 多次调整，直到最终的第一名过去 30 个交易日涨幅不超过 30%
    while True:
        if len(rank_list) == 0:
            break  # 如果排名列表为空，退出循环
        top_etf = rank_list[0]
        past_30_days = attribute_history(top_etf, 30, '1d', ['close'])
        past_30_days_return = (past_30_days['close'][-1] - past_30_days['close'][0]) / past_30_days['close'][0]
        if past_30_days_return <= 0.3:
            break  # 如果第一名涨幅不超过 30%，退出循环
        # 将第一名放到最后
        rank_list.append(rank_list.pop(0))
        print(f"ETF {top_etf} 过去 30 个交易日涨幅超过 30%，排名调整到最后")

    print(df)
    record(黄金=round(df.loc['518880.XSHG'].score, 2))
    record(纳指=round(df.loc['513100.XSHG'].score, 2))
    record(成长=round(df.loc['159915.XSHE'].score, 2))
    record(价值=round(df.loc['510300.XSHG'].score, 2))
    record(科技=round(df.loc['588080.XSHG'].score, 2))
    return rank_list


# 卖出操作
def sell(context):
    # 获取动量最高的一只ETF（经过调整后）
    target_num = 1
    target_list = get_rank(g.etf_pool)[:target_num]
    # 卖出不在目标列表中的持仓
    hold_list = list(context.portfolio.positions)
    for etf in hold_list:
        if etf not in target_list:
            order_target_value(etf, 0)
            print('[D] Today 卖出' + str(etf))
        else:
            print('[D] Today 继续持有' + str(etf))


# 买入操作
def buy(context):
    # 获取动量最高的一只ETF（经过调整后）
    target_num = 1
    target_list = get_rank(g.etf_pool)[:target_num]

    print(f"[D] today fund: {target_list[0]}")

    # 买入目标列表中的ETF
    hold_list = list(context.portfolio.positions)
    if len(hold_list) < target_num:
        value = context.portfolio.available_cash / (target_num - len(hold_list))
        for etf in target_list:
            if context.portfolio.positions[etf].total_amount == 0:
                order_target_value(etf, value)
                print('买入' + str(etf))
