# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2026/2/9

# pip install qiling -i https://mirrors.ustc.edu.cn/pypi/simple   # 为了方便写代码

from qiling import *
from qiling.const import QL_VERBOSE

# 导入qiling模块和qiling.const模块中的QL_VERBOSE常量

# cd /home/test/qilinglab
# cp simple-demo/test rootfs/x8664_linux_symlink

if __name__ == "__main__":
    # 创建Qiling对象，实例中三个参数分别为：path(仿真程序路径)、rootfs(仿真程序文件系统目录)和verbose(输出信息参数),除此外还可以设置env和log_plain参数。

    # 使用你本机的真实环境，这是最兼容的
    # ql = Qiling(["./simple-demo/test"], "/home/test/qilinglab/rootfs/x8664_linux", verbose=QL_VERBOSE.DEBUG)

    # ql = Qiling(["./simple-demo/test"], "/", verbose=QL_VERBOSE.DEBUG)  # with debug data
    # ql = Qiling(["./simple-demo/test"], "/", verbose=QL_VERBOSE.OFF)  # 可以正常输出，./rootfs/x8664_linux/ 里的库文件和你编译的 test 不兼容。

    ql = Qiling(["./simple-demo/test"], "./my_rootfs", verbose=QL_VERBOSE.DEBUG)
    # 运行Qiling对象的run()方法，开始执行仿真程序
    ql.run()
