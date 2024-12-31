# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/17 15:01'

"""
ElementTree是Python提供解析xml的标准库
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484059&idx=1&sn=2eb49643a14c4068d994f86dcd3d0e95&scene=19#wechat_redirect
"""

try:
    # 若想加快速度，可以使用C语言编译的API xml.etree.cElementTree。
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# 读、增、修改、删除操作
print("Element Tree XPath特性支持示例:")

# 加载xml文件
tree = ET.parse('data_demo.xml')

# 获取根节点, 并打印节点文本：data
root = tree.getroot()
print("并打印节点文本: ", end="")
print(root.tag)

# 遍历输出country及其name属性
for child in root:
    print(child.tag, "name：", child.attrib["name"])

# 遍历rank节点
# 我们借助iter迭代器来进行全迭代查找感兴趣的节点
# 输出节点tag及其文本
print("使用iter迭代器查找目标节点:")
for rank in root.iter("rank"):
    print(rank.tag, "-", rank.text)

print("遍历gdppc节点：")
for gd in root.iter("gdppc"):
    print(gd.tag, "-", gd.text)

# 换一种方式来遍历rank节点
# 我们借助findall和find方法来查找感兴趣的节点
# 输出节点tag及其文本
# 注意：findall只能查找从当前节点的子节点查找目标节点
print("使用findall查找目标节点")
# 使用findall查找所有country节点，用于遍历
for country in root.findall("country"):
    #print(country)
    # 使用find从country节点中查找rank节点
    rank = country.find("rank")
    print(rank.tag, " - ", rank.text)

# 把所有的rank的文本都修改为： 学习Python
for rank in root.iter("rank"):
    rank.text = "学习Python"
    rank.set('updated', 'yes')

# 把修改后的rank的文本重新遍历打印出来，这时应该打印出： 学习Python
for rank in root.iter("rank"):
    print(rank.text)

print("新增节点：")

# 给所有的country新增一个<url>www.fullstackpentest.com</url>节点,
for country in root.iter("country"):
    # 创建一个节点
    url = ET.Element("url")   # <url> 和<country>节点同级
    # print(url)

    # 给节点url的text赋值
    url.text = "www.fullstackpentest.com"

    # 将url节点追加到country节点下
    country.append(url)

print("检查是否添加url节点成功:")
# 打印下整个xml出来看看是不是所有country节点都新增了一个url节点
for country in root.iter("country"):
    # 查找url节点
    url = country.find("url")

    # 打印url的text
    print(url.text)

# 删除year节点
print("删除year节点:")
for country in root.iter("country"):
    year = country.find("year")

    # 如果year节点存在，则删除
    if year is not None:
        print("删除了一个year节点")
        country.remove(year)

# 保存上述 修改、新增、删除后的xml到 data_demo_new.xml中
# 打开data_demo_new.xml文档看修改、新增、删除的节点是否有效
tree.write("data_demo_new.xml", encoding="utf-8")


