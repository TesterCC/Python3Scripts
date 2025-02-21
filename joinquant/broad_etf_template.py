# 导入函数库
from jqdata import *

# 初始化函数，设定基准等等
def initialize(context):
    # 设定基准
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option("use_real_price", True)

    ### 场外基金相关设定 ###
    # 设置账户类型: 场外基金账户
    set_subportfolios([SubPortfolioConfig(context.portfolio.cash, 'open_fund')])
    # 设置赎回到账日
    set_redeem_latency(3, 'QDII_fund')

    ## 运行函数（reference_security为运行时间的参考标的；传入的标的只做种类区分，因此传入'000300.XSHG'或'510300.XSHG'是一样的）
        # 开盘时运行
    run_daily(market_open, time='open', reference_security='000300.XSHG')
        # 收盘后运行
    run_daily(after_market_close, time='after_close', reference_security='000300.XSHG')

def market_open(context):
    # 设置场外基金标的为景顺沪深300('000311.OF')
    s = '000311.OF'

    # 获取基金信息
    fund_info = get_fund_info(s)
    log.info("基金名称：",fund_info['fund_name'])

    # 确定时间是周几
    weekday = context.current_dt.isoweekday()
    log.info("今天是周 %s" % weekday)
    # 申购基金
    if weekday == 1:
        o = purchase(s, 10000)
        log.info(o)
    # 赎回基金
    elif weekday == 3:
        o1 = redeem(s, 4000)
        log.info(o1)
    elif weekday == 4:
        o2 = redeem(s, 3000)
        log.info(o2)

## 收盘后运行函数
def after_market_close(context):
    # 查看融资融券账户相关相关信息(更多请见API-对象-SubPortfolio)
    p = context.portfolio.subportfolios[0]
    log.info('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    log.info('查看场外基金账户相关相关信息(更多请见API-对象-SubPortfolio)：')
    log.info('场外基金持有份额：',p.long_positions['000311.OF'].closeable_amount)
    log.info('账户所属类型：',p.type)
    log.info('##############################################################')
