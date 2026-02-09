from qiling import *
# 测试qilinglab是否能正常在linux64启动
if __name__ == '__main__':
    path = ["qilinglab-x86_64"]
    rootfs = "rootfs/x8664_linux"
    ql = Qiling(path, rootfs)
    ql.run()
