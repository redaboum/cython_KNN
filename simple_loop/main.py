from time import time

from cython_loop import cython_loop
from python_loop import python_loop

t1 = time()

python_loop()

t2 = time()

cython_loop()

t3 = time()

print("looping with python takes : " + str(t2 - t1))
print("looping with cython takes : " + str(t3 - t2))