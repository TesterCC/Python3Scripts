from distutils.core import setup
from Cython.Build import cythonize

'''
要将Python3代码编译为.so文件并在Python3中导入该文件，可以使用Cython和ctypes模块的组合。

步骤如下：

1.安装Cython：可以使用pip安装Cython：pip install cython (注意名称)

2.创建一个.pyx文件：将Python代码保存为一个.pyx文件，它将被Cython编译为C代码。

3.编写setup.py文件：在同一目录中创建一个setup.py文件，用于编译并生成共享对象文件。
setup.py文件通常包含以下内容：见下方

4.在终端中运行以下命令：python setup.py build_ext --inplace
此命令将在当前目录中生成共享对象文件。

5.在Python3中导入库：可以使用ctypes模块导入.so文件并调用其中的函数。示例见call_demo.py
'''

#　cythonize函数将编译demo.pyx文件并生成共享对象文件。
setup(
    ext_modules=cythonize("demo.pyx")
)
