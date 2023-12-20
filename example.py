from data_type import *

a = uint8(255)
b = uint8(1)
print(a + b) # 0

a = int8(127)
b = int8(1)
print(a + b) # -128

a = uint8(-1)
print(a) # 255

a = vec([1, 2, 3])
b = vec([4, 5, 6])
print(a + b) # vec([5, 7, 9])

a = vec([[1, 2, 3], [4, 5, 6]])
b = vec([[7, 8, 9], [10, 11, 12]])
print(a + b) # vec([[8, 10, 12], [14, 16, 18]])
print(a * b) # vec([[7, 16, 27], [40, 55, 72]])