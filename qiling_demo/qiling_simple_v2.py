# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2026/2/9

from qiling import *
from qiling.const import QL_VERBOSE
import os

if __name__ == "__main__":
    # 使用绝对路径更稳妥
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    binary_path = os.path.join(cur_dir, "simple-demo/test")
    rootfs_path = os.path.join(cur_dir, "my_rootfs")

    # 初始化 Qiling
    # ql = Qiling([binary_path], rootfs_path, verbose=QL_VERBOSE.DEBUG)
    ql = Qiling([binary_path], rootfs_path, verbose=QL_VERBOSE.OFF)

    # 【关键步骤】手动映射核心库文件
    # 格式：ql.add_fs_mapper(虚拟路径, 宿主机真实路径)
    # 这样当程序在模拟器里找 /lib64/libc.so.6 时，Qiling 会强制去读宿主机的真实文件
    ql.add_fs_mapper("/lib64/libc.so.6", "/usr/lib64/libc.so.6")
    ql.add_fs_mapper("/lib64/ld-linux-x86-64.so.2", "/lib64/ld-linux-x86-64.so.2")

    # 如果还有其他报错缺少的库，也可以照此添加
    # ql.add_fs_mapper("/etc/ld.so.cache", "/etc/ld.so.cache")

    print("[*] 正在启动仿真...")
    ql.run()


    """
    
Qiling 的虚拟文件系统（VFS）在尝试打开这个文件时被拒绝了。

这通常是由于 CentOS/RHEL 系统中 /lib64 到 /usr/lib64 的复杂**符号链接（Symlink）**导致的路径解析冲突。即使你用了 cp -L，Qiling 内部的路径重定向逻辑有时仍会陷入死循环或权限迷宫。

终极方案：使用 add_fs_mapper 强制映射
既然 rootfs="/" 能跑通，说明你的宿主机库文件是没问题的。为了在自定义 rootfs 下也能运行，我们可以使用 Qiling 的 VFS 强制映射功能。这会跳过所有复杂的目录搜索，直接把虚拟环境里的库路径“粘”到宿主机的真实文件上。
    """