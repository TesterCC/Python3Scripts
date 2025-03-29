def twos_complement_to_decimal(binary_str):
    # 将二进制字符串转换为整数
    num = int(binary_str, 2)
    # 判断符号位
    if binary_str[0] == '1':
        # 32位补码负数的计算
        return num - (1 << 32)
    return num

# 示例二进制数
binary = '10000000000000000000000000000000'
decimal = twos_complement_to_decimal(binary)
print(f"二进制数 {binary} 对应的十进制数是 {decimal}")
