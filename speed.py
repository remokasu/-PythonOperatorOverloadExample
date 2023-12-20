from data_type import *
import timeit

def f1():
    n = 100000
    p = 0
    for k in range(n):
        p += (-1) ** k * (2 * k + 1) / (2 * k + 1)
    p *= 4
    return p

def f2():
    n = 100000
    p = real(0)
    for k in range(n):
        p += (-1) ** k * (2 * k + 1) / (2 * k + 1)
    p *= 4
    return p

# 計測
elapsed_time_f1 = timeit.timeit(f1, number=1)
elapsed_time_f2 = timeit.timeit(f2, number=1)

print("f1: " + str(elapsed_time_f1) + "[sec]")
print("f2: " + str(elapsed_time_f2) + "[sec]")
print("f2/f1: " + str(elapsed_time_f2/elapsed_time_f1))

r = f2()
print(type(r))
