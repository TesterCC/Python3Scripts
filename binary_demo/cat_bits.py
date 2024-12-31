# -*- coding:utf-8 -*-
def concatenate_bits(bit_list):
    # 初始化结果为0
    result = 0

    # 逐个遍历bit_list中的每个bit值，并拼接到结果中
    for bit in bit_list:
        # 将结果左移一位，给新的bit腾出位置
        result <<= 1
        # 如果当前bit为1，则将其设置到结果的最低位
        if bit == 1:
            result |= 1

    return result


# 示例：拼接一个字节的数据：1 0 1 1 0 1 0 0
bit_list = [1, 0, 1, 1, 0, 1, 0, 0]
result_byte = concatenate_bits(bit_list)
print("Result Byte (Decimal):", result_byte)  # 输出结果字节的十进制表示

# 将结果字节转换为二进制字符串并显示
result_binary = bin(result_byte)
print("Result Byte (Binary):", result_binary)  # 输出结果字节的二进制表示
