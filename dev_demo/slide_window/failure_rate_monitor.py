from collections import deque

'''
实现使用滑动窗口记录一个窗口内的失败请求比率，超过 20% 就不再重试的代码。
 
Python 代码
    deque 用于实现滑动窗口，其 maxlen 参数可以限制窗口的大小。
    simulate_request 函数模拟请求，随机返回成功或失败。
    sliding_window_failure_rate 函数实现了滑动窗口的逻辑，每次请求后更新窗口，计算失败率，若超过阈值则停止重试。
    
Go实现：
/learngo/dev_demo/slide_window/failure_rate_monitor.go
'''

def simulate_request():
    # 模拟请求，这里简单随机返回成功或失败
    import random
    return random.random() < 0.8


def sliding_window_failure_rate(max_retries, window_size, failure_threshold):
    window = deque(maxlen=window_size)
    for attempt in range(max_retries):
        success = simulate_request()
        window.append(not success)
        failure_rate = sum(window) / len(window)
        if failure_rate > failure_threshold:
            print(f"Failure rate {failure_rate * 100:.2f}% exceeds threshold, stopping retries.")
            break
        if success:
            print("Request succeeded.")
            return
    print("Max retries reached without success.")


if __name__ == '__main__':

    # 参数设置
    max_retries = 10
    window_size = 5
    failure_threshold = 0.2

    sliding_window_failure_rate(max_retries, window_size, failure_threshold)
