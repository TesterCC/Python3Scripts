# -*- coding=utf-8 -*-

import json

# P182 6.2.3 要符合JSON规范，应只对Python列表和字典进行编码
# JSON编码格式几乎与Python语法一致，区别是：Python中True会被映射为 true，False会被映射为 false， None会被映射为 null

print(json.dumps(False))
demo = {'a': True, 'b': 'Hello', 'd': False, 'c': None}
print(json.dumps(demo))

# P184 输出中对key排序
print(json.dumps(demo, sort_keys=True))

# P184 输出格式美化
print(json.dumps(demo, indent=4))

