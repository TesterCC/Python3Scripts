# coding=utf-8
"""
DATE:   2022/3/17
AUTHOR: TesterCC
"""

'''
ref: https://www.cnblogs.com/jiangxiaobo/p/12481852.html
ref: https://www.cnblogs.com/dream4567/p/8862182.html
ref: https://www.cnblogs.com/liuhui0308/p/12665600.html

UUID（Universally Unique Identifier）是通用唯一识别码，在许多领域用作标识

python有一个模块叫做uuid，导入它就可以使用它的四个方法了。
注意这四个方法依次是uuid1(),uuid3(),uuid4(),uuid5()
是的，没有uuid2()……

# uuid1(): 这个是根据当前的时间戳和MAC地址生成的，最后的12个字符408d5c985711对应的就是MAC地址，因为是MAC地址。
# uuid3(): 里面的namespace和具体的字符串都需要指定，通过md5生成。
# uuid4(): 基于随机数的uuid，既然是随机就有可能真的遇到相同的，但几率很小，因为随机且方便，一般使用频率较高。
# uuid5(): 这个看起来和uuid3()貌似并没有什么不同，写法一样，是由用户来指定namespace和字符串，不过这里用的散列并不是MD5，而是SHA1。
'''

import uuid

# usage example

print(uuid.uuid1())

print(uuid.uuid3(uuid.NAMESPACE_DNS,'TesT'))

print(uuid.uuid4())

print(uuid.uuid5(uuid.NAMESPACE_DNS,'TesT'))


# 去掉uuid中的'-'
tuid = uuid.uuid4()
print(str(tuid).replace("-",""))