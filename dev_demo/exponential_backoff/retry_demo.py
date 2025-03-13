# -*- coding:utf-8 -*-
'''
指数退避策略（Exponential Backoff）是一种用于控制重试频率的算法，常见于网络请求、分布式系统或资源竞争场景中。
其核心思想是：当请求失败时，后续重试的等待时间按指数级增长，从而避免立即重复尝试导致的系统压力或资源耗尽。

常见变种

1.带抖动的退避：在指数时间基础上添加随机波动（如 ±1 秒），避免所有客户端同步重试。
2.最大等待时间：设置上限（如 30 秒），防止无限等待。


应用场景：
    网络请求：API 调用失败时，避免频繁重试加重服务端负担。
    分布式锁：多个节点竞争资源时，减少冲突概率。
    任务调度：任务执行失败后，逐步增加重试间隔。

优势：
    平衡系统负载，提高整体稳定性。
    给予服务恢复的时间窗口（如临时故障）。
    降低重试风暴（Retry Storm）风险。

go版本见：
learngo/dev_demo/ExponentialBackoff/ExBackoff.go
'''


import time
import random

max_retries = 5 #  最大重试次数
base_delay = 1  # 初始延迟1秒

def launch_task():
    # mock task
    # e.g. url request and so on
    print("mock run task")
    # 触发失败后retry
    return False

for attempt in range(max_retries):
    try:
        # 执行请求或操作
        result = launch_task()
        if not result:
            raise RuntimeError
        break
    except Exception:
        if attempt == max_retries - 1:
            raise "Max retries exceeded"
        # 计算延迟时间（指数退避 + 抖动）
        delay = base_delay * (2 ** attempt)
        delay += random.uniform(0, 1)  # 添加0-1秒的随机抖动
        print(f"[D] retry delay time: {delay}")
        time.sleep(delay)
