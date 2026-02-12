# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2026/2/10


import sys
sys.path.append("..")

from qiling import Qiling
from qiling.const import QL_VERBOSE

# 可以运行 一个 16 位 DOS 二进制文件, windows10/11不能直接 Linux的qiling可以运行

if __name__ == "__main__":
    ql = Qiling(["rootfs/8086/dos/HI.DOS_COM"], "rootfs/8086/dos", verbose=QL_VERBOSE.DEFAULT)
    ql.run()
