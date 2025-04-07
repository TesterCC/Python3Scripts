# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='print_module',
    ext_modules=cythonize('print_module.pyx'),
)