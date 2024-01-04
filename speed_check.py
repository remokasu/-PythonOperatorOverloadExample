import numpy as np
import timeit

from data_type import *

# + vs np.add

a = np.random.rand(1000)
b = np.random.rand(1000)

def using_plus():
    return a + b

def using_np_add():
    return np.add(a, b)

plus_time = timeit.timeit(using_plus, number=10000)
np_add_time = timeit.timeit(using_np_add, number=10000)

print(f"+: {plus_time}")
print(f"np.add: {np_add_time}")


# =====================================

a = Real(1.919)
b = Real(2.919)

_a = 1.919
_b = 2.919

def using_plus():
    return a + b

def using_np_add():
    return np.add(a, b)

def using_default_plus():
    return _a + _b

plus_time = timeit.timeit(using_plus, number=10000)
np_add_time = timeit.timeit(using_np_add, number=10000)
default_plus_time = timeit.timeit(using_default_plus, number=10000)

print(f"+: {plus_time}")
print(f"np.add: {np_add_time}")
print(f"default +: {default_plus_time}")
