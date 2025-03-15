# -*- coding:utf-8 -*-
# pip install bloom-filter2

import asyncio
from bloom_filter2 import BloomFilter
import random

'''
使用布隆过滤器实现 100 万 QPS 抢 10 万券的幂等性方案
1.布隆过滤器的初始化
在抢券活动开始前，需要初始化布隆过滤器。布隆过滤器的大小和哈希函数的数量会影响误判率，需要根据实际情况进行调整。
可以使用 Python 的 bloom-filter 库来实现。
2.抢券逻辑
当有抢券请求到来时，首先检查该用户 ID 是否在布隆过滤器中，如果不在则进行抢券逻辑，抢券成功后（或完成抢券行为后）将该用户 ID 插入布隆过滤器。
3. 高并发处理
在实际的高并发场景中，需要使用多线程或异步编程来处理大量的抢券请求。可以使用 Python 的 asyncio 库来实现异步处理。

总结：
通过使用布隆过滤器，可以在高并发的抢券场景中高效地判断用户是否已经抢到券，从而保证抢券操作的幂等性。
虽然布隆过滤器存在一定的误判率，但在这种场景下是可以接受的。
同时，为了提高系统的性能，还需要结合多线程或异步编程来处理大量的请求。

go线程安全加锁的参考版本：
~/learngo/bloom_filter_demo/bf_demo.go
'''

# 预计插入的元素数量   # mock 10万库存
capacity = 100000
# 期望的误判率
error_rate = 0.001

# 初始化布隆过滤器
bloom = BloomFilter(max_elements=capacity, error_rate=error_rate)

async def grab_coupon(user_id):
    # 检查用户是否已经抢到券
    if user_id in bloom:
        print(f"用户 {user_id} 已经抢到券，本次请求被拒绝。")
        return False
    # 模拟抢券逻辑，这里简单随机判断是否抢券成功
    # random.random()用于生成随机浮点数。其生成的数据范围为 [0.0, 1.0)，即包含 0.0，但不包含 1.0。
    if random.random() < 0.1:  # 假设抢券成功率为 10%
        # 抢券成功，将用户 ID 插入布隆过滤器
        bloom.add(user_id)
        print(f"用户 {user_id} 抢券成功！")
        return True
    else:
        print(f"用户 {user_id} 抢券失败。")
        return False

async def main():
    tasks = []
    # 模拟 100 万次抢券请求
    for i in range(1000000):
        # 对 100000 取模，这样可以保证在 100 万次循环中，用户 ID 会在 user_0 到 user_99999 这 10 万个不同的用户 ID 之间循环，从而模拟 10 万个用户发起抢券请求。
        user_id = f"user_{i % 100000}"  # 模拟 10 万个用户
        # asyncio.create_task 是一个异步编程的函数，用于创建一个异步任务。这里将 grab_coupon(user_id) 这个异步函数调用封装成一个任务对象 task。
        # grab_coupon 函数是之前定义的用于处理单个用户抢券逻辑的异步函数。
        task = asyncio.create_task(grab_coupon(user_id))
        tasks.append(task)

    # asyncio.gather 是一个异步编程的函数，用于并发地运行多个异步任务。
    # *tasks 是解包操作，将 tasks 列表中的所有任务对象作为独立的参数传递给 asyncio.gather。
    # await 关键字用于暂停 main 函数的执行，直到所有任务都完成。也就是说，程序会等待所有 100 万个抢券任务都执行完毕后，才会继续执行 main 函数后续的代码（如果有的话）。
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Python 3.7 及以上版本中用于运行异步程序（函数或协程）的一种便捷方式。管理整个事件循环的生命周期，包括启动事件循环、执行传入的异步函数以及在函数执行完成后关闭事件循环。
    # asyncio.run() 函数只能在主线程中调用，不能在已经运行着事件循环的线程中再次调用。
    # 在一个程序中，同一时间只能有一个事件循环处于运行状态，asyncio.run() 会确保这一点，避免出现多个事件循环冲突的问题。
    asyncio.run(main())
