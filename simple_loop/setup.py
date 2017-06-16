from distutils.core import setup
from Cython.Build import cythonize

setup(name="cython_loop", ext_modules=cythonize('cython_loop.pyx'),)