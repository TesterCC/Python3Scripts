import time

try:
    future_time = 2_200_01_01_00_00_00  # 2200-01-01 00:00:00 UTC（远超 2038 年）
    print("未来时间戳:", future_time)
    print("转换结果:", time.ctime(future_time))
except OverflowError as e:
    print("发生溢出错误:", e)