import numpy as np
import pandas as pd
import math


def initialize(context):
    g.etf_pool = ['518880.XSHG', '513100.XSHG', '159915.XSHE', '510300.XSHG', '588080.XSHG']
    g.m_days = 20
    g.top_n = 2
    set_benchmark('000300.XSHG')
    set_order_cost(OrderCost(open_tax=0, close_tax=0, open_commission=0.0003, close_commission=0.0003), type='fund')
    set_slippage(FixedSlippage(0))
    run_daily(trade, time='9:40')


def trade(context):
    current_data = get_current_data()
    for etf in g.etf_pool:
        if current_data[etf].paused:
            log.warn(f"{etf} 停牌，跳过今日交易")
            return
    rank_list = get_rank(g.etf_pool)
    buy_list = rank_list[:g.top_n]

    # 卖出不在买入列表中的持仓
    for etf in context.portfolio.positions:
        if etf not in buy_list:
            order_target_value(etf, 0)

    # 买入逻辑
    if buy_list:
        weight = 1.0 / len(buy_list)
        cash_per_etf = context.portfolio.total_value * weight
        for etf in buy_list:
            order_target_value(etf, cash_per_etf)


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
    print(df)
    record(黄金=round(df.loc['518880.XSHG'], 2))
    record(纳指=round(df.loc['513100.XSHG'], 2))
    record(成长=round(df.loc['159915.XSHE'], 2))
    record(价值=round(df.loc['510300.XSHG'], 2))
    record(科技=round(df.loc['588080.XSHG'], 2))
    return rank_list