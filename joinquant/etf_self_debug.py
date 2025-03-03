# 导入函数库
from jqdata import *
from jqfactor import Factor, calc_factors
import datetime
import numpy as np

'''
ETF动量趋势轮动

里面有几个品种黄金、纳指、创业板、沪深300、科创板，
为什么选这几个？因为前提是宽基，另外相关性要小，这样才有可能涨跌不同步
豆粕和黄金是一个性质的，所以不用同时加入轮动, 如果加豆粕，就把黄金从列表中删除
#record(豆粕 = round(df.loc['159985.XSHE'], 2))
'''


# 策略初始化
def initialize(context):
    g.etf_pool = ['518880.XSHG', '513100.XSHG', '159915.XSHE', '510300.XSHG', '588080.XSHG']
    g.m_days = 25  # or 24
    g.top_n = 2
    set_benchmark('000300.XSHG')
    set_order_cost(OrderCost(open_tax=0, close_tax=0, open_commission=0.0003, close_commission=0.0003), type='fund')
    set_slippage(FixedSlippage(0))
    run_daily(trade, time='9:40')


# 可以将买入和卖出操作单独用 def buy() 和 def sell()实现，也可以把操作逻辑都写到def trade()中
def trade(context):
    current_data = get_current_data()
    for etf in g.etf_pool:
        if current_data[etf].paused:
            log.warn(f"{etf} 停牌，跳过今日交易")
            return
    rank_list = get_rank(g.etf_pool)
    buy_list = rank_list[:g.top_n]

    # 卖出不在买入列表中的持仓
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

    # 买入逻辑
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