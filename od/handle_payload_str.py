# coding=utf-8
"""
DATE:   2021/3/22
AUTHOR: Yanxi Li
"""

s = "%u6750%u565a%u5566%u7a6f%u6551%u5450%u6f54%u7a62%u4653%u6b41%u1806%u101f%u828c%u1083%u0d7b%u103e%u8002%u102d%u876b%u1003%u0001%u1004%u0001%u0000%u6917%u104e%u1000%u0000%uc000%u102a%u0040%u0000%u0005%u102e%uc001%u102a%u1806%u101f%u9090%u9090%u3401%u102b%u0cbc%u0c0c%ubb0c%ufe0f%u53c6%udddb%u74d9%uf424%u2958%ub1c9%u834b%ufce8%u5831%u030e%uf057%ua624%ue49b%u4926%uf563%u7b58%u91b1%u2913%ud105%uc276%ub7ee%u5362%ubc15%u4bf9%u3ce4%u3cf2%ue54c%u833c%ud5fc%u7f5f%u09fe%ube80%u5c31%u87c1%u2a84%u552e%u5e41%u4ae2%u22e6%u6a3f%u2928%u147f%uee4d%ua8f4%u3f4c%u687f%ube6e%ud953%u88e5%u5f4b%u7c30%u1650%u82f3%u9c23%u7d78%uece2%ubfbe%u02c5%u4192%u241d%u340a%u5655%u4fb7%u24ae%uc563%u8e31%u7de0%u2e96%u1b25%u3c5d%u6f82%u2139%ua315%u5d31%u429e%ud796%u60e4%ub332%u09bf%u1963%u356e%uc573%u93cf%ue4ff%ua306%uf6ff%uf927%u3b97%u02e5%u5468%u707e%ufb5a%u1ed4%u74d6%ud9f2%u926f%u3505%uf3d7%ub6f8%udd28%ue23e%u7578%u8b97%u8512%u5e18%u8f8e%ua18e%ubce7%u4ac9%ubcfa%ud6c4%u5a73%ub6b6%uf3d3%u6776%ua394%u6d1e%u9b1b%u8e3e%ub4f1%u61d4%uedac%u1b40%u66f5%ue4f1%u0323%u6e31%uf3c0%u87ff%ue7ad%u6797%u5af8%u7731%uf1d6%uedbd%u53dd%u99ea%u82df%u05dc%ue11f%u8f57%u4ab5%uf00f%u4b59%ua6cf%u4b33%u1ea7%u1860%u60d2%u0cbd%uf54f%u653e%u5e3c%u8b57%ua81b%u74f8%u284e%ua2c4%u5eb6%u7724"

# "%u0000"
ptrs = "%u0048%u0c00%u704d%u7867%u4243%u6948%u714d%u4350%u705a%u6546%u5642%u6d6d%u6d61%u4572%u4b59%u5557%u486f%u7765%u0000%u26f0%u104c%u7a56%u4563%u0000%u240c%u3410%u007c%u0c00%u5326%u1005%u6862%u4458%u4678%u6d52%u6d64%u4e47%u536c%u526f%u734c%u4164%u6572%u4452%u7545%u737a%u554a%u774a%u585a%u6758%u6a4c%u4477%u7256%u4364%u002e%u0c00"

head = 0
next = 0

jump = 12

#
for i in range(len(s)//jump):
    print(s[i*jump:i*jump+jump])

# for i in range(len(ptrs) // jump):
#     print(ptrs[i * jump:i * jump + jump])




