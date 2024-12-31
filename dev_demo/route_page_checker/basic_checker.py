import re

# 输入的字符串
input_string = """
baseUrl: '//www.juniper.net/documentation/us/en/software/jweb-srx22.4/help/jweb-srx',
url: '//www.juniper.net/documentation/us/en/software/jweb-srx22.4/help/jweb-srx',
"""

# 定义正则表达式模式
pattern = r'jweb-srx(\d+\.\d+)'

# 使用 re 模块进行匹配
match = re.search(pattern, input_string)

# 检查是否有匹配项
if match:
    version_number = match.group(1)
    print("提取的版本号是:", version_number)
else:
    print("未找到匹配项")
