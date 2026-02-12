# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2026/2/10

import sys
sys.path.append("..")

from qiling import Qiling
from qiling.const import QL_VERBOSE

# cd /home/test/qiling/examples
# fail, lack dependency
if __name__ == "__main__":
    # initialize Qiling instance, specifying the executable to emulate and the emulated system root.
    # note that the current working directory is assumed to be Qiling home
    ql = Qiling([r'rootfs/x86_windows/bin/x86_hello.exe'], r'rootfs/x86_windows', verbose=QL_VERBOSE.DEFAULT)

    # start emulation
    ql.run()