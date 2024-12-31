import ctypes

import ctypes

# 加载共享对象文件
demo_lib = ctypes.CDLL('./example.so')

# 调用共享对象文件中的函数
result = demo_lib.add_numbers(4, 6)

# 打印结果
print(result)

# test output
demo_lib.output_time()