def format_mac_address(mac_address):
    mac_address = mac_address.upper()
    # 移除输入中的非十六进制字符
    cleaned_mac = ''.join(c for c in mac_address if c.isalnum())

    # 将MAC地址分组，每组两个字符
    formatted_mac = ':'.join(cleaned_mac[i:i + 2] for i in range(0, len(cleaned_mac), 2))

    return formatted_mac


if __name__ == '__main__':
    # 输入的MAC地址
    mac_address_input = '000c29d8514f'

    # 转换为标准格式
    formatted_mac_address = format_mac_address(mac_address_input)

    # 打印结果
    print("转换后的MAC地址:", formatted_mac_address)
