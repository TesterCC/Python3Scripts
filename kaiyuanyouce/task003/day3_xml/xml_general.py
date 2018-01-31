__author__ = 'MFC'
__time__ = '18/1/31 07:10'

"""
加深

封装一个xml通用解析类，实现以下能力：

1.支持xpath提取或设置指定节点值
2.支持遍历指定节点
3.支持读取或设置指定节点的属性
"""

import re

# 导入ElementTree

try:
    # 若想加快速度，可以使用C语言编译的API xml.etree.cElementTree
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class XmlTool(object):
    """
    兼容xml string和 .xml
    """

    def __init__(self, data):
        self._attr = None
        self._xpath = None
        self.data = data
        self.root = None

        m = re.search(".*.xml$", self.data)   # 普通匹配

        if m:
            print(".xml Match Success")
            # 从文件加载xml，获取xml tree节点
            tree = ET.parse(self.data)

            # 获取根节点
            self.root = tree.getroot()

            # 打印下根节点的节点tag， 输出data
            print("root node: %s" % self.root.tag)
        else:
            print(".xml Match Failed")
            # 从字符串加载xml
            root = ET.fromstring(self.data)

            # 打印下根节点的节点tag， 输出data
            print("root node: %s" % self.root.tag)

    def get_node_obj(self):
        """
        获取根节点下所有的对象
        """
        da = self.root.findall(".")
        for d in da:
            print(d.tag)

    def find_node_by_xpath(self, xpath):
        """
        支持xpath提取或设置指定节点值
        """
        if isinstance(xpath, str):
            self._xpath = xpath

        return self._xpath

    def get_specific_node(self, xpath):
        """
        支持遍历指定节点 输出指定节点属性
        """
        self.find_node_by_xpath(xpath)
        childs = self.root.findall(self._xpath)
        for child in childs:
            print(child.tag, " ", child.attrib, "     ", child.text)

    # @property
    # def node_attr(self):
    #     """
    #     支持读取指定节点的属性
    #     """
    #     for self.child in self.childs:
    #         for i in self.child:
    #             print(i)
    #     return
    #
    # @node_attr.setter
    # def node_attr(self, nodetag, value):
    #     """
    #     支持设置指定节点的属性
    #     """
    #     if isinstance(value, str):
    #         self._attr = value

    def modify(self, nodetag, value, exp_value):
        """
        支持读取或设置指定节点的属性
        修改下节点的text试试
        """
        for child in self.root.iter(nodetag):
            if child.text == value:
                child.text = exp_value
                child.set('updated', 'yes')

        # 打印下修改后的xml所有的year节点
        print("修改后：")
        for child in self.root.iter(nodetag):
            # 打印出year节点的tag和text
            print(child.tag, " ", child.text)


if __name__ == '__main__':

    # data = """
    # <data>
    # <country name="Liechtenstein">
    #     <rank>1</rank>
    #     <year>2008</year>
    #     <gdppc>141100</gdppc>
    #     <neighbor name="Austria" direction="E"/>
    #     <neighbor name="Switzerland" direction="W"/>
    # </country>
    # <country name="Singapore">
    #     <rank>4</rank>
    #     <year>2011</year>
    #     <gdppc>59900</gdppc>
    #     <neighbor name="Malaysia" direction="N"/>
    # </country>
    # <country name="Panama">
    #     <rank>68</rank>
    #     <year>2011</year>
    #     <gdppc>13600</gdppc>
    #     <neighbor name="Costa Rica" direction="W"/>
    #     <neighbor name="Colombia" direction="E"/>
    # </country>
    # </data>
    # """

    # filename = "cnvd.xml"
    filename = "xml_data.xml"
    xt = XmlTool(filename)

    # xt.get_node_obj()

    print("支持遍历指定节点和内容:")
    # xt.get_specific_node(".//number")
    # xt.get_specific_node(".//title")
    # xt.get_specific_node(".//neighbor")
    xt.get_specific_node(".//year")
    print("-" * 80)
    xt.modify("year", "2008", "1998")
    xt.modify("year", "2011", "2021")









